// -*- C++ -*-
// AUTHOR:  Anil Singh (anil@cern.ch), Lovedeep Saini (lovedeep@cern.ch)
// Modified for 2011 7TeV muon-only analysis for wjets with jet pt/eta, D Baumgartel (darinb@cern.ch)

#include "Rivet/Analysis.hh"
#include "Rivet/RivetAIDA.hh"
#include "Rivet/Tools/Logging.hh"
#include "Rivet/Projections/FinalState.hh"
#include "Rivet/Projections/FastJets.hh"
#include "Rivet/Projections/VetoedFinalState.hh"
#include "Rivet/Projections/InvMassFinalState.hh"
#include "Rivet/Tools/ParticleIdUtils.hh"
#include "Rivet/Projections/MissingMomentum.hh"
#include "TTree.h"
#include "TFile.h"
#include "TString.h"
#include <iostream>
#include <ostream>
#include <iomanip>
namespace Rivet
{

	class CMS_SMP_12_23 : public Analysis
	{
		public:

			// Definition of the analysis, with pp collisions
			CMS_SMP_12_23()
				: Analysis("CMS_SMP_12_23")
			{
				setBeams(PROTON, PROTON);
				setNeedsCrossSection(true);
			}

			// Book histograms and initialise projections before the run
			void init()
			{

				// ------------------------------------------------------- //
				// ----------------  The Rivet Projections  -------------- //
				// ------------------------------------------------------- //
				// The total final state
				const FinalState fs(-MAXRAPIDITY,MAXRAPIDITY);
				addProjection(fs, "FS");

				// Projection for the missing energy
				MissingMomentum missing(fs);
				addProjection(missing, "MET");

				// Constructing the W final state with a muon
				vector<pair<PdgId,PdgId> > vidsW;
				vidsW.push_back(make_pair(MUON, NU_MUBAR));
				vidsW.push_back(make_pair(ANTIMUON, NU_MU));

				FinalState fsW(-MAXRAPIDITY,MAXRAPIDITY);
				InvMassFinalState invfsW(fsW, vidsW, 0.0*GeV, 999999*GeV);
				addProjection(invfsW, "INVFSW");

				// Constructing the vetoed final state
				VetoedFinalState vfs(fs);
				vfs.addVetoOnThisFinalState(invfsW);
				addProjection(vfs, "VFS");
				addProjection(FastJets(vfs, FastJets::ANTIKT, 0.5), "Jets");

				// ------------------------------------------------------- //
				// ----------------  RESULTS AS HISTOGRAMS --------------- //
				// ------------------------------------------------------- //

				// Inclusive and exclusive jet multiplicity
				_histJetMultWmu       = bookHistogram1D("njetWmunu", 6, 0.5, 6.5);
				_histJetMultWmuInc    = bookHistogram1D("njetWmunuInc", 6, 0.5, 6.5);

				// The pT of the four leading jets
				_histJetPT1Wmu    = bookHistogram1D("JetPT1Wmunu", 26,30,300);
				_histJetPT2Wmu    = bookHistogram1D("JetPT2Wmunu", 26,30,300);
				_histJetPT3Wmu    = bookHistogram1D("JetPT3Wmunu", 13,30,300);
				_histJetPT4Wmu    = bookHistogram1D("JetPT4Wmunu", 13,30,300);

				// The HT for jet multiplicities of 1 to 4
				_histJetHT1Wmu    = bookHistogram1D("JetHT1Wmunu", 26,30,300);
				_histJetHT2Wmu    = bookHistogram1D("JetHT2Wmunu", 26,30,300);
				_histJetHT3Wmu    = bookHistogram1D("JetHT3Wmunu", 13,30,300);
				_histJetHT4Wmu    = bookHistogram1D("JetHT4Wmunu", 13,30,300);

				// The pseudorapidity of the four leading jets
				_histJetETA1Wmu    = bookHistogram1D("JetETA1Wmunu", 12,-2.4,2.4);
				_histJetETA2Wmu    = bookHistogram1D("JetETA2Wmunu", 12,-2.4,2.4);
				_histJetETA3Wmu    = bookHistogram1D("JetETA3Wmunu", 12,-2.4,2.4);
				_histJetETA4Wmu    = bookHistogram1D("JetETA4Wmunu", 12,-2.4,2.4);

				// The DeltaPhi between the nth leading jet and the muon, n = 1,2,3,4
				_histJetMuDphi1Wmu    = bookHistogram1D("JetMuDphi1Wmunu", 12,-2.4,2.4);
				_histJetMuDphi2Wmu    = bookHistogram1D("JetMuDphi2Wmunu", 12,-2.4,2.4);
				_histJetMuDphi3Wmu    = bookHistogram1D("JetMuDphi3Wmunu", 12,-2.4,2.4);
				_histJetMuDphi4Wmu    = bookHistogram1D("JetMuDphi4Wmunu", 12,-2.4,2.4);

				// ------------------------------------------------------- //
				// ----------------  RESULTS AS A TTree ------------------ //
				// ------------------------------------------------------- //
				_treeFileName = "rivetTree.root";
				// Create a file for the Tree
				_treeFile = new TFile(_treeFileName, "recreate");

				// Book the ntuple.
				_rivetTree = new TTree("RivetTree", "RivetTree");

				// Add Branches
				_rivetTree->Branch("nevt", &_nevt, "nevt/I");
				_rivetTree->Branch("evweight", &_evweight, "evweight/D");

				_rivetTree->Branch("njet_WMuNu", &_njet_WMuNu, "njet_WMuNu/I");
				_rivetTree->Branch("mt_munu", &_mt_munu, "mt_munu/D");
				_rivetTree->Branch("mt_mumet", &_mt_mumet, "mt_mumet/D");

				_rivetTree->Branch("htjets", &_htjets, "htjets/D");
				_rivetTree->Branch("ptmuon", &_ptmuon, "ptmuon/D");
				_rivetTree->Branch("etamuon", &_etamuon, "etamuon/D");
				_rivetTree->Branch("phimuon", &_phimuon, "phimuon/D");

				_rivetTree->Branch("ptneutrino", &_ptneutrino, "ptneutrino/D");
				_rivetTree->Branch("etaneutrino", &_etaneutrino, "etaneutrino/D");
				_rivetTree->Branch("phineutrino", &_phineutrino, "phineutrino/D");

				_rivetTree->Branch("ptmet", &_ptmet, "ptmet/D");
				_rivetTree->Branch("phimet", &_phimet, "phimet/D");

				_rivetTree->Branch("ptjet1", &_ptjet1, "ptjet1/D");
				_rivetTree->Branch("ptjet2", &_ptjet2, "ptjet2/D");
				_rivetTree->Branch("ptjet3", &_ptjet3, "ptjet3/D");
				_rivetTree->Branch("ptjet4", &_ptjet4, "ptjet4/D");

				_rivetTree->Branch("etajet1", &_etajet1, "etajet1/D");
				_rivetTree->Branch("etajet2", &_etajet2, "etajet2/D");
				_rivetTree->Branch("etajet3", &_etajet3, "etajet3/D");
				_rivetTree->Branch("etajet4", &_etajet4, "etajet4/D");

				_rivetTree->Branch("dphijet1muon", &_dphijet1muon, "dphijet1muon/D");
				_rivetTree->Branch("dphijet2muon", &_dphijet2muon, "dphijet2muon/D");
				_rivetTree->Branch("dphijet3muon", &_dphijet3muon, "dphijet3muon/D");
				_rivetTree->Branch("dphijet4muon", &_dphijet4muon, "dphijet4muon/D");

			}

			double DeltaPhi(double phi1, double phi2)
			{
				double pi = 3.14159265358;
				double dphi = fabs(phi1-phi2);
				if (dphi>pi) dphi = 2.0*pi-dphi;
				return dphi;
			}

			bool ApplyMuonCutsForWmn(double pt1, double eta1,double mt)
			{
				bool isFid1 = ((fabs(eta1)<2.1));
				if( isFid1 && pt1>25. && mt>50.) return true;
				return 0;
			}

			void FillWithValue(AIDA::IHistogram1D*& _hist, const double& weight, const double &value)
			{
				_hist->fill(value, weight);
			}

			void analyze(const Event& event)
			{

				// Check gen particles to flag events with a W decaying to mu nu from the hard interaction
				bool WdecayToMuNu = false;
				bool has_muon_status3 = false;
				bool has_numu_status3 = false;
				foreach (GenParticle* p, Rivet::particles(event.genEvent()))
				{
					int st = p->status();
					int pdg = p->pdg_id();
					if ((st==3) && abs(pdg)==13) has_muon_status3 = true;
					if ((st==3) && abs(pdg)==14) has_numu_status3 = true;
				}

				if (has_muon_status3 && has_numu_status3) WdecayToMuNu = true;

				// Initialize Values
				bool isWmn =false;

				_mt_munu = -5.0;
				_ptmuon = -5.0;
				_etamuon = -5.0;
				_phimuon = -5.0;
				_ptmet = -5.0;
				_phimet = -5.0;
				_mt_mumet = -5.0;
				_htjets = 0.0;

				_ptneutrino = -1.0;
				_etaneutrino = -5.0;
				_phineutrino = -5.0;

				_ptjet1 = -5.0;
				_etajet1 = -5.0;
				_dphijet1muon = -1.0;
				_ptjet2 = -5.0;
				_etajet2 = -5.0;

				_dphijet2muon = -1.0;
				_ptjet3 = -5.0;
				_etajet3 = -5.0;

				_dphijet3muon = -1.0;
				_ptjet4 = -5.0;
				_etajet4 = -5.0;
				_dphijet4muon = -1.0;

				_njet_WMuNu = -1;
				_nBjet_WMuNu = -1;

				_evweight = -1.0;
				_nevt = -1;

				// Recording of event weight and numbers
				const double weight = event.weight();
				_nevt = (event.genEvent()).event_number();
				_evweight = weight;

				// The W Final State
				const InvMassFinalState& invMassFinalStateW = applyProjection<InvMassFinalState>(event, "INVFSW");

				// The total final state
				const FinalState& totalfinalstate = applyProjection<FinalState>(event, "FS");

				bool isW = (!(invMassFinalStateW.empty()));
				if (!isW) vetoEvent;
				if (!WdecayToMuNu) vetoEvent;

				// Vector of W decay product particles and vector of all particles
				const ParticleVector&  WDecayProducts =  invMassFinalStateW.particles();
				const ParticleVector& AllParticles = totalfinalstate.particles();

				// Recording of W decay product variables
				// "1" will be for neutrino, and "2" for muon
				double pt1=-9999.,  pt2=-9999.;
				double phi1=-9999., phi2=-9999.;
				double eta1=-9999., eta2=-9999.;
				double mt = 999999;

				// Get the missing momentum
				const MissingMomentum& met = applyProjection<MissingMomentum>(event, "MET");
				_ptmet = met.visibleMomentum().pT();
				_phimet = met.visibleMomentum().phi();
				_phimet -= 3.1415926;
				if (_phimet < 0.0) _phimet += 2.0*3.1415926;
				_mt_mumet = sqrt(2.0*_ptmuon*_ptmet*(1.0-cos(_phimet-_phimuon)));

				// Look at events with W
				if(isW)
				{
					// For the case of leading-particle as muon
					if(fabs(WDecayProducts[1].pdgId()) == NU_MU)
					{
						pt1  = WDecayProducts[0].momentum().pT();
						pt2  = WDecayProducts[1].momentum().Et();
						eta1 = WDecayProducts[0].momentum().eta();
						eta2 = WDecayProducts[1].momentum().eta();
						phi1 = WDecayProducts[0].momentum().phi();
						phi2 = WDecayProducts[1].momentum().phi();
						mt=sqrt(2.0*pt1*pt2*(1.0-cos(phi1-phi2)));
						_mt_mumet=sqrt(2.0*pt1*_ptmet*(1.0-cos(phi1-_phimet)));
					}
					// For the case of leading particle as neutrino
					else
					{
						pt1  = WDecayProducts[1].momentum().pT();
						pt2  = WDecayProducts[0].momentum().Et();
						eta1 = WDecayProducts[1].momentum().eta();
						eta2 = WDecayProducts[0].momentum().eta();
						phi1 = WDecayProducts[1].momentum().phi();
						phi2 = WDecayProducts[0].momentum().phi();
						mt=sqrt(2.0*pt1*pt2*(1.0-cos(phi1-phi2)));
						_mt_mumet=sqrt(2.0*pt2*_ptmet*(1.0-cos(phi2-_phimet)));

					}
				}

				// Boolean to determine that we are in the W->MuNu final state
				isWmn  = isW && ((fabs(WDecayProducts[0].pdgId()) == 14) || (fabs(WDecayProducts[1].pdgId()) == 14));
				if(!isWmn) vetoEvent;

				// Enforce the generator-level phase space ()
				bool passBosonConditions = false;
				if(isWmn) passBosonConditions = ApplyMuonCutsForWmn(pt1,eta1,_mt_mumet);
				if(!passBosonConditions) vetoEvent;

				// Calculating Kinemetic Quantities in the W->MuNu final state

				// Determine the index of WDecayProducts which is the muon and neutrino
				int muind = -1;
				int nuind=-1;
				if (fabs(WDecayProducts[0].pdgId()) == 13) muind = 0;
				if (fabs(WDecayProducts[1].pdgId()) == 13) muind = 1;
				nuind = 1*(muind==0);

				// Get the muon and neutrino momenta, and the transverse mass of the mu
				_mt_munu = mt;
				_ptmuon  = WDecayProducts[muind].momentum().pT();
				_etamuon = WDecayProducts[muind].momentum().eta();
				_phimuon = WDecayProducts[muind].momentum().phi();
				_ptneutrino  = WDecayProducts[nuind].momentum().pT();
				_etaneutrino = WDecayProducts[nuind].momentum().eta();
				_phineutrino = WDecayProducts[nuind].momentum().phi();

				// Muon Four-Momentum
				FourMomentum finalmuon(WDecayProducts[muind].momentum());

				// Initialize a pseudojet vector to store jet input particles with no neutrinos and cleaned from
				// From photons around the muon
				std::vector<fastjet::PseudoJet> input_particles_nonu_dresscleaned;

				// Loop over all particles
				for (unsigned int nn = 0; nn<AllParticles.size(); nn++)
				{
					// Get particle PDGId and four-momentum
					unsigned int _nn_pid = abs(AllParticles[nn].pdgId());
					const FourMomentum p4 = AllParticles[nn].momentum();

					// Get pseudo-jet of individual particle, and calculate dR w.r.t. muon
					fastjet::PseudoJet p_seudo = fastjet::PseudoJet(p4.px(), p4.py(), p4.pz(), p4.E());
					double dr = deltaR(AllParticles[nn].momentum(),WDecayProducts[muind].momentum());

					// If it is a photon within a cone of 0.1, add particle to the muon
					if ((_nn_pid == 22) && (dr<0.1)) finalmuon = add(finalmuon,AllParticles[nn].momentum());

					// Determine whether the particle is suitable for a jet
					// True by default
					bool keep_part_for_jet = true;
					// If it was a photon used to dress the muon, discard it
					if ((_nn_pid == 22) && (dr<0.1)) keep_part_for_jet = false;
					// If the particle is a neutrino, discard it
					if ((_nn_pid == 12)||(_nn_pid == 14)||(_nn_pid == 16)) keep_part_for_jet = false;
					// If the particle is the muon, discard it
					if (_nn_pid == 13) keep_part_for_jet = false;

					// Add particle to set of jet particle candidates
					if (keep_part_for_jet) input_particles_nonu_dresscleaned.push_back(p_seudo);

				}

				// Switch the muon kinematics to the dressed-muon values
				_ptmuon  = finalmuon.pT();
				_etamuon = finalmuon.eta();
				_phimuon = finalmuon.phi();

				//Vectors to store jet quantities
				vector<float> finaljet_pT_list;
				vector<float> finaljet_eta_list;
				vector<float> finaljet_phi_list;

				// Runt he clustering on the jet candidate particles with no neutrinos and no dressed-muon photons. Sort by pT.
				fastjet::ClusterSequence cseq(input_particles_nonu_dresscleaned, fastjet::JetDefinition(fastjet:: antikt_algorithm, 0.5));
				vector<fastjet::PseudoJet> jets_filtered = sorted_by_pt(cseq.inclusive_jets(0.0));

				// Loop over filtered jets to remove jets not passing kinematic criteria.
				for (unsigned int ij = 0; ij < jets_filtered.size(); ij++)
				{
					// Jet pT/Eta/Phi
					double jpt = jets_filtered[ij].perp();
					double jeta = jets_filtered[ij].eta();
					double jphi = jets_filtered[ij].phi();

					// Kinemetic cuts for jet acceptance
					if ((fabs(jeta) < 2.4) && (jpt>30))
					{
						// Get DeltaEta and DeltaPhi w.r.t. muon
						double delta_phi = fabs(DeltaPhi(_phimuon,jphi));
						double delta_eta = fabs(_etamuon-jeta);

						// Only pass jets which are dR>0.5 from the muon
						if( (delta_eta*delta_eta) + (delta_phi*delta_phi) > 0.25  )
						{
							// Add jet to jet list and increases the HT variable
							finaljet_pT_list.push_back(jpt);
							finaljet_eta_list.push_back(jeta);
							finaljet_phi_list.push_back(jphi);
							_htjets += fabs(jpt);
						}
					}
				}

				//Multiplicity plots.
				if(isWmn)FillWithValue(_histJetMultWmu, weight, finaljet_pT_list.size());

				if((isWmn)&&(finaljet_pT_list.size()>=1)) FillWithValue(_histJetPT1Wmu,weight,finaljet_pT_list[0]);
				if((isWmn)&&(finaljet_pT_list.size()>=2)) FillWithValue(_histJetPT2Wmu,weight,finaljet_pT_list[1]);
				if((isWmn)&&(finaljet_pT_list.size()>=3)) FillWithValue(_histJetPT3Wmu,weight,finaljet_pT_list[2]);
				if((isWmn)&&(finaljet_pT_list.size()>=4)) FillWithValue(_histJetPT4Wmu,weight,finaljet_pT_list[3]);

				if((isWmn)&&(finaljet_pT_list.size()>=1)) FillWithValue(_histJetETA1Wmu,weight,finaljet_eta_list[0]);
				if((isWmn)&&(finaljet_pT_list.size()>=2)) FillWithValue(_histJetETA2Wmu,weight,finaljet_eta_list[1]);
				if((isWmn)&&(finaljet_pT_list.size()>=3)) FillWithValue(_histJetETA3Wmu,weight,finaljet_eta_list[2]);
				if((isWmn)&&(finaljet_pT_list.size()>=4)) FillWithValue(_histJetETA4Wmu,weight,finaljet_eta_list[3]);

				_njet_WMuNu = finaljet_pT_list.size();

				if (finaljet_pT_list.size()>0)
				{
					_ptjet1=finaljet_pT_list[0];
					_etajet1=finaljet_eta_list[0];
					_dphijet1muon = DeltaPhi(finaljet_phi_list[0],_phimuon);
				}

				if (finaljet_pT_list.size()>1)
				{
					_ptjet2=finaljet_pT_list[1];
					_etajet2=finaljet_eta_list[1];
					_dphijet2muon = DeltaPhi(finaljet_phi_list[1],_phimuon);
				}

				if (finaljet_pT_list.size()>2)
				{
					_ptjet3=finaljet_pT_list[2];
					_etajet3=finaljet_eta_list[2];
					_dphijet3muon = DeltaPhi(finaljet_phi_list[2],_phimuon);
				}

				if (finaljet_pT_list.size()>3)
				{
					_ptjet4=finaljet_pT_list[3];
					_etajet4=finaljet_eta_list[3];
					_dphijet4muon = DeltaPhi(finaljet_phi_list[3],_phimuon);
				}

				_rivetTree->Fill();

			}

			// Write the tree.
			void finalize()
			{
				_rivetTree->Write();
				_treeFile->Close();
			}

		private:

			AIDA::IHistogram1D*  _histJetMultWmu ;
			AIDA::IHistogram1D*  _histJetMultWmuInc ;

			AIDA::IHistogram1D*  _histJetPT1Wmu ;
			AIDA::IHistogram1D*  _histJetPT2Wmu ;
			AIDA::IHistogram1D*  _histJetPT3Wmu ;
			AIDA::IHistogram1D*  _histJetPT4Wmu ;

			AIDA::IHistogram1D*  _histJetHT1Wmu ;
			AIDA::IHistogram1D*  _histJetHT2Wmu ;
			AIDA::IHistogram1D*  _histJetHT3Wmu ;
			AIDA::IHistogram1D*  _histJetHT4Wmu ;

			AIDA::IHistogram1D*  _histJetETA1Wmu ;
			AIDA::IHistogram1D*  _histJetETA2Wmu ;
			AIDA::IHistogram1D*  _histJetETA3Wmu ;
			AIDA::IHistogram1D*  _histJetETA4Wmu ;

			AIDA::IHistogram1D*  _histJetMuDphi1Wmu ;
			AIDA::IHistogram1D*  _histJetMuDphi2Wmu ;
			AIDA::IHistogram1D*  _histJetMuDphi3Wmu ;
			AIDA::IHistogram1D*  _histJetMuDphi4Wmu ;

			TTree* _rivetTree;
			TString _treeFileName;
			TFile* _treeFile;

			int _nevt;
			int _njet_WMuNu;
			int _nBjet_WMuNu;

			double _evweight;

			double _mt_munu;
			double _mt_mumet;
			double _htjets;
			double _ptmet;
			double _phimet;

			double _ptmuon;
			double _etamuon;
			double _phimuon;

			double _ptneutrino;
			double _etaneutrino;
			double _phineutrino;

			double _ptjet1;
			double _ptjet2;
			double _ptjet3;
			double _ptjet4;

			double _etajet1;
			double _etajet2;
			double _etajet3;
			double _etajet4;

			double _dphijet1muon;
			double _dphijet2muon;
			double _dphijet3muon;
			double _dphijet4muon;

	};

	AnalysisBuilder<CMS_SMP_12_23> plugin_CMS_SMP_12_23;

}
