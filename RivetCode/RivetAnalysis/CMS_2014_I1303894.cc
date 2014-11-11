// -*- C++ -*-
// AUTHOR:  Darin Baumgartel (darinb@cern.ch) - Last mod: Aug 29, 2014
// Based on Rivet analysis originally created by Anil Singh (anil@cern.ch), Lovedeep Saini (lovedeep@cern.ch)

#include "Rivet/Analysis.hh"
#include "Rivet/Tools/Logging.hh"
#include "Rivet/Projections/FinalState.hh"
#include "Rivet/Projections/FastJets.hh"
#include "Rivet/Projections/VetoedFinalState.hh"
#include "Rivet/Projections/InvMassFinalState.hh"
#include "Rivet/Tools/ParticleIdUtils.hh"
#include "Rivet/Projections/MissingMomentum.hh"
#include "Rivet/Projections/WFinder.hh"
#include "Rivet/Projections/DressedLeptons.hh"
#include <iostream>
#include <ostream>
#include <iomanip>
namespace Rivet {

  class CMS_2014_I1303894 : public Analysis {
    public:

      // Definition of the analysis, with pp collisions
      CMS_2014_I1303894(): Analysis("CMS_2014_I1303894") {
      }


      // Book histograms and initialise projections before the run
      void init() {
        // ------------------------------------------------------- //
        // ----------------  The Rivet Projections  -------------- //
        // ------------------------------------------------------- //

        const FinalState fs(-MAXDOUBLE,MAXDOUBLE);
        addProjection(fs, "FS");

        MissingMomentum missing(fs);
        addProjection(missing, "MET");

        IdentifiedFinalState bareMuons(fs);
        bareMuons.acceptIdPair(PID::MUON);
        DressedLeptons muonClusters(fs, bareMuons, 0.1, false, -MAXDOUBLE,MAXDOUBLE,0.0,false);
        addProjection(muonClusters, "muonClusters");

        IdentifiedFinalState neutrinos(-MAXDOUBLE, MAXDOUBLE, 0.0*GeV);
        neutrinos.acceptIdPair(PID::NU_MU);
        addProjection(neutrinos, "neutrinos");
          
        VetoedFinalState jetFS(fs);
        jetFS.addVetoOnThisFinalState(muonClusters);
        jetFS.addVetoOnThisFinalState(neutrinos);
        jetFS.vetoNeutrinos();
        FastJets JetProjection(jetFS,FastJets::ANTIKT,0.5);
        JetProjection.useInvisibles(false);
        addProjection(JetProjection, "Jets");

        // ------------------------------------------------------- //
        // ----------------  RESULTS AS HISTOGRAMS --------------- //
        // ------------------------------------------------------- //

        _histDPhiMuJet1 = bookHisto1D(1,1,1);
        _histDPhiMuJet2 = bookHisto1D(2,1,1);
        _histDPhiMuJet3 = bookHisto1D(3,1,1);
        _histDPhiMuJet4 = bookHisto1D(4,1,1);

        _histEtaJet1 = bookHisto1D(5,1,1);
        _histEtaJet2 = bookHisto1D(6,1,1);
        _histEtaJet3 = bookHisto1D(7,1,1);
        _histEtaJet4 = bookHisto1D(8,1,1);

        _histHT1JetInc = bookHisto1D(9,1,1);
        _histHT2JetInc = bookHisto1D(10,1,1);
        _histHT3JetInc = bookHisto1D(11,1,1);
        _histHT4JetInc = bookHisto1D(12,1,1);

        _histJet30MultExc  = bookHisto1D(13,1,1);
        _histJet30MultInc  = bookHisto1D(14,1,1);

        _histPtJet1 = bookHisto1D(15,1,1);
        _histPtJet2 = bookHisto1D(16,1,1);
        _histPtJet3 = bookHisto1D(17,1,1);
        _histPtJet4 = bookHisto1D(18,1,1);

        _n_1jet  = 0.0;
        _n_2jet  = 0.0;
        _n_3jet  = 0.0;
        _n_4jet  = 0.0;
        _n_inclusivebinsummation = 0.0;
      }


      void analyze(const Event& event) {
        // Get the dressed muon
        const DressedLeptons& muonClusters = applyProjection<DressedLeptons>(event, "muonClusters");
        int nmu = muonClusters.clusteredLeptons().size();
        if (nmu<1) vetoEvent;
        DressedLepton dressedmuon=muonClusters.clusteredLeptons()[0];
        if ( fabs(dressedmuon.momentum().eta())>2.1 ) vetoEvent;
        if ( fabs(dressedmuon.momentum().pT())<25.0 ) vetoEvent;

        // Get the muon neutrino
        const Particles& neutrinos = applyProjection<FinalState>(event, "neutrinos").particlesByPt();
        int nnumu = neutrinos.size();
        if (nnumu < 1) vetoEvent;

        // Check that the muon and neutrino are not decay products of tau
        if (dressedmuon.constituentLepton().hasAncestor(-16)) vetoEvent;
        if (dressedmuon.constituentLepton().hasAncestor(-15)) vetoEvent;
        if (dressedmuon.constituentLepton().hasAncestor(15)) vetoEvent;
        if (dressedmuon.constituentLepton().hasAncestor(16)) vetoEvent;
        if (neutrinos[0].hasAncestor(-16)) vetoEvent;
        if (neutrinos[0].hasAncestor(-15)) vetoEvent;
        if (neutrinos[0].hasAncestor(15)) vetoEvent;
        if (neutrinos[0].hasAncestor(16)) vetoEvent;

        // Recording of event weight and numbers
        const double weight = event.weight();

        // Get the missing momentum
        const MissingMomentum& met = applyProjection<MissingMomentum>(event, "MET");
        double _ptmet = met.visibleMomentum().pT();
        double _phimet = (-met.visibleMomentum()).phi();

        // Calculate MET and MT(mu,MET), and remove events with MT<50
        double _ptmuon = dressedmuon.momentum().pT();
        double _phimuon = dressedmuon.momentum().phi();
        double _mt_mumet = sqrt(2.0*_ptmuon*_ptmet*(1.0-cos(_phimet-_phimuon)));

        // Remove events in MT<50 region 
        if (_mt_mumet<50.) vetoEvent;

        //Loop over jets and fill pt/eta/phi quantities in vectors
        const Jets& jets_filtered = applyProjection<FastJets>(event, "Jets").jetsByPt(0.0*GeV);
        vector<float> finaljet_pT_list, finaljet_eta_list, finaljet_phi_list;
        double _htjets = 0.0;

        for (unsigned int ii = 0; ii < jets_filtered.size(); ++ii) {
          // Jet pT/Eta/Phi
          double jet_pt = jets_filtered[ii].perp();
          double jet_eta = jets_filtered[ii].eta();
          double jet_phi = jets_filtered[ii].phi();

          // Kinemetic cuts for jet acceptance
          if (fabs(jet_eta) > 2.4) continue;
          if (jet_pt < 30.0) continue;
          if (deltaR(dressedmuon.momentum(),jets_filtered[ii])<0.5) continue;

          // Add jet to jet list and increases the HT variable
          finaljet_pT_list.push_back(jet_pt);
          finaljet_eta_list.push_back(jet_eta);
          finaljet_phi_list.push_back(jet_phi);
          _htjets += fabs(jet_pt);  
        }

        // ------------------------------------------------------------
        // ------------ Filling of histograms below -------------------
        // ------------------------------------------------------------

        // Fill as many jets as there are into the exclusive jet multiplicity
        if ((finaljet_pT_list.size()) >=1) {
          _histJet30MultExc -> fill(finaljet_pT_list.size(), weight);
        }

        for (unsigned int ij = 0; ij < finaljet_pT_list.size(); ++ij) {
          _histJet30MultInc -> fill(ij+1, weight);
          _n_inclusivebinsummation += weight;
        }

        if (finaljet_pT_list.size()>=1) {
          _histPtJet1 -> fill(finaljet_pT_list[0],weight);
          _histEtaJet1 -> fill(fabs(finaljet_eta_list[0]), weight);
          _histDPhiMuJet1 -> fill(deltaPhi(finaljet_phi_list[0],_phimuon),weight);
          _histHT1JetInc -> fill(_htjets, weight);
          _n_1jet +=weight;
        }

        if (finaljet_pT_list.size()>=2) {
          _histPtJet2 -> fill(finaljet_pT_list[1], weight);
          _histEtaJet2 -> fill(fabs(finaljet_eta_list[1]), weight);
          _histDPhiMuJet2 -> fill(deltaPhi(finaljet_phi_list[1],_phimuon), weight);
          _histHT2JetInc -> fill(_htjets, weight);
          _n_2jet += weight;
        }

        if (finaljet_pT_list.size()>=3) {
          _histPtJet3 -> fill(finaljet_pT_list[2], weight);
          _histEtaJet3 -> fill(fabs(finaljet_eta_list[2]), weight);
          _histDPhiMuJet3 -> fill(deltaPhi(finaljet_phi_list[2],_phimuon), weight);
          _histHT3JetInc -> fill(_htjets, weight);
          _n_3jet += weight;
        }        

        if (finaljet_pT_list.size()>=4) {
          _histPtJet4 -> fill(finaljet_pT_list[3], weight);
          _histEtaJet4 -> fill(fabs(finaljet_eta_list[3]), weight);
          _histDPhiMuJet4 -> fill(deltaPhi(finaljet_phi_list[3],_phimuon), weight);
          _histHT4JetInc-> fill(_htjets, weight);
          _n_4jet += weight;
        }        

      }

      // Finalize the histograms.
      void finalize() {
        
        double inclusive_cross_section = 31314.0;
        double norm_1jet_histo = inclusive_cross_section*_n_1jet/sumOfWeights();
        double norm_2jet_histo = inclusive_cross_section*_n_2jet/sumOfWeights();
        double norm_3jet_histo = inclusive_cross_section*_n_3jet/sumOfWeights();
        double norm_4jet_histo = inclusive_cross_section*_n_4jet/sumOfWeights();
        double norm_incmultiplicity = inclusive_cross_section*_n_inclusivebinsummation/sumOfWeights();

        normalize(_histJet30MultExc, norm_1jet_histo);
        normalize(_histJet30MultInc, norm_incmultiplicity);

        normalize(_histPtJet1, norm_1jet_histo);
        normalize(_histHT1JetInc, norm_1jet_histo);
        normalize(_histEtaJet1, norm_1jet_histo);
        normalize(_histDPhiMuJet1, norm_1jet_histo);

        normalize(_histPtJet2, norm_2jet_histo);
        normalize(_histHT2JetInc, norm_2jet_histo);
        normalize(_histEtaJet2, norm_2jet_histo);
        normalize(_histDPhiMuJet2, norm_2jet_histo);

        normalize(_histPtJet3, norm_3jet_histo);
        normalize(_histHT3JetInc, norm_3jet_histo);        
        normalize(_histEtaJet3, norm_3jet_histo);
        normalize(_histDPhiMuJet3, norm_3jet_histo);

        normalize(_histPtJet4, norm_4jet_histo);
        normalize(_histHT4JetInc, norm_4jet_histo);        
        normalize(_histEtaJet4, norm_4jet_histo);
        normalize(_histDPhiMuJet4, norm_4jet_histo);                

      }

    private:

      Histo1DPtr  _histJet30MultExc;
      Histo1DPtr  _histJet30MultInc;

      Histo1DPtr  _histPtJet1;
      Histo1DPtr  _histPtJet2;
      Histo1DPtr  _histPtJet3;
      Histo1DPtr  _histPtJet4;

      Histo1DPtr  _histEtaJet1;
      Histo1DPtr  _histEtaJet2;
      Histo1DPtr  _histEtaJet3;
      Histo1DPtr  _histEtaJet4;

      Histo1DPtr  _histDPhiMuJet1;
      Histo1DPtr  _histDPhiMuJet2;
      Histo1DPtr  _histDPhiMuJet3;
      Histo1DPtr  _histDPhiMuJet4;

      Histo1DPtr  _histHT1JetInc;
      Histo1DPtr  _histHT2JetInc;
      Histo1DPtr  _histHT3JetInc;
      Histo1DPtr  _histHT4JetInc;

      double _n_1jet;
      double _n_2jet;
      double _n_3jet;
      double _n_4jet;
      double _n_inclusivebinsummation;

  };

  DECLARE_RIVET_PLUGIN(CMS_2014_I1303894);

}
