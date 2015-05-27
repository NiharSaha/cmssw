#include <iostream>
#include <fstream>
#include "Fireworks/Core/interface/FWPartialConfig.h"
#include "TGButton.h"
#include "TEveManager.h"
#include "TGString.h"
#include "TGLabel.h"
#include "Fireworks/Core/src/SimpleSAXParser.h"
#include "Fireworks/Core/interface/FWXMLConfigParser.h"
#include "Fireworks/Core/interface/FWEventItemsManager.h"
#include "Fireworks/Core/interface/FWGUIManager.h"
#include "Fireworks/Core/interface/FWConfigurationManager.h"

namespace {
struct MyNameMap {
    std::vector< std::pair<std::string, std::string> > names = { { "GUI", "Windows" }, { "CommonPreferences", "Colors" }, { "EventNavigator" , "EventFilters" },   { "EventItems" , "Collections" } };

    std::string realName(std::string btnName)
    {
        for (std::vector< std::pair<std::string, std::string> >::iterator i = names.begin(); i!= names.end(); ++i) {
            if (i->second == btnName) 
                return i->first;
        }
        return btnName;
    }


    std::string btnName(const std::string& rlName)
    {

        for (std::vector< std::pair<std::string, std::string> >::iterator i = names.begin(); i!= names.end(); ++i) {
            if (i->first == rlName) 
                return i->second;
        }
        return rlName;
    }
};

    MyNameMap nmm;
}


//---------------------------------------------------------------------
//---------------------------------------------------------------------
//---------------------------------------------------------------------
//---------------------------------------------------------------------

FWPartialConfigGUI::FWPartialConfigGUI( const char* path, FWConfigurationManager* iCfg):
    TGMainFrame(gClient->GetRoot(), 200, 140), m_cfgMng(iCfg)
{
    if (path) {
        std::ifstream g(path);
        FWXMLConfigParser parser(g);
        parser.parse();
        parser.config()->swap(m_origConfig);
    }
    else {
        printf("------------- dumping current configuration \n");
        FWConfiguration curr;
        m_cfgMng->to(curr);
        curr.swap(m_origConfig);
    }

    TGVerticalFrame* vf = new TGVerticalFrame(this);
    AddFrame(vf, new TGLayoutHints(kLHintsNormal, 2, 2, 4, 4));

    for(FWConfiguration::KeyValues::const_iterator it = m_origConfig.keyValues()->begin(); it != m_origConfig.keyValues()->end(); ++it) {
        if ( it->second.keyValues()) {
            std::string nb =  nmm.btnName(it->first);
            printf("itfirst %s kv = %p  sv = %p \n", it->first.c_str(), it->second.keyValues(), it->second.stringValues());


            TGCheckButton* cb = new TGCheckButton(vf, nb.c_str());
            vf->AddFrame(cb);

            m_entries.push_back(cb);
        }
    }
}
//---------------------------------------------------------------------
//---------------------------------------------------------------------
//---------------------------------------------------------------------
//---------------------------------------------------------------------

FWPartialConfigLoadGUI::FWPartialConfigLoadGUI( const char* path, FWConfigurationManager* iCfg, FWEventItemsManager* iEiMng):
    FWPartialConfigGUI(path, iCfg), m_eiMng(iEiMng)
{
   TGHorizontalFrame* hf = new TGHorizontalFrame(this);
   AddFrame(hf, new TGLayoutHints( kLHintsRight| kLHintsBottom, 1, 1, 2, 4));
   TGTextButton* load = new TGTextButton(hf, " Load ");
   load->Connect("Clicked()", "FWPartialConfigLoadGUI", this, "Load()");
   hf->AddFrame(load, new TGLayoutHints(kLHintsExpandX, 2, 2, 0, 0));
   TGTextButton* cancel = new TGTextButton(hf, " Cancel ");
   cancel->Connect("Clicked()", "FWPartialConfigLoadGUI", this, "Cancel()");
   hf->AddFrame(cancel, new TGLayoutHints(kLHintsExpandX, 2, 2, 0, 0));
   
   SetWindowName("Load Config");
   MapSubwindows();
   Layout();
   MapWindow();
}

FWPartialConfigLoadGUI::~FWPartialConfigLoadGUI() 
{
}

void FWPartialConfigLoadGUI::Load()
{   
    bool resetViews = true;
    bool resetEI = true;
    
    FWConfiguration::KeyValues* kv = (FWConfiguration::KeyValues*)m_origConfig.keyValues();
    
    for (auto i = m_entries.begin(); i != m_entries.end(); i++) {    
        if (!((*i)->IsOn())) {
            std::string key =  nmm.realName((*i)->GetText()->GetString());
            if (key == "EventItems") resetEI = false;
            if (key == "GUI") resetViews = false;

            for(FWConfiguration::KeyValues::iterator it = kv->begin(); it != kv->end(); ++it)
            {
                if ( key.compare(it->first) == 0) {
                    kv->erase(it);
                    break;
                }
            }
        } 
    }

    if (resetEI)
       m_eiMng->clearItems();

    if (resetViews)
        FWGUIManager::getGUIManager()->subviewDestroyAll();

    gEve->DisableRedraw();
    m_cfgMng ->setFrom(m_origConfig);
    gEve->EnableRedraw();

    UnmapWindow();
}


void FWPartialConfigLoadGUI::Cancel()
{
    // AMT should not there be a destroy ??
    UnmapWindow();
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
//---------------------------------------------------------------------
//---------------------------------------------------------------------

FWPartialConfigSaveGUI::FWPartialConfigSaveGUI( const char* path_out, FWConfigurationManager* iCfg):
    FWPartialConfigGUI(0, iCfg), m_outFileName(path_out)
{
    printf("partial save  %s !!!! \n",   path_out );
    
   TGHorizontalFrame* hf = new TGHorizontalFrame(this);
   AddFrame(hf, new TGLayoutHints( kLHintsRight| kLHintsBottom, 1, 1, 2, 4));
   
   TGTextButton* write = new TGTextButton(hf, " Write ");
   write->Connect("Clicked()", "FWPartialConfigSaveGUI", this, "Write()");
   hf->AddFrame(write, new TGLayoutHints(kLHintsExpandX, 2, 2, 0, 0));

   TGTextButton* cancel = new TGTextButton(hf, " Cancel ");
   cancel->Connect("Clicked()", "FWPartialConfigSaveGUI", this, "Cancel()");
   hf->AddFrame(cancel, new TGLayoutHints(kLHintsExpandX, 2, 2, 0, 0));

   AddFrame(new TGLabel(this, Form("File: %s", path_out)),  new TGLayoutHints(kLHintsLeft, 8,2,4,2));
  
   SetWindowName("Save Config");

   MapSubwindows();
   Layout();
   MapWindow();
}

void
FWPartialConfigSaveGUI::Cancel()
{
    UnmapWindow();
}


void
FWPartialConfigSaveGUI::Write()
{
    printf("--------------write\n");
    
    FWConfiguration destination;
    {
        std::ifstream g(m_outFileName.c_str());
        if (g.peek() == (int) '<') {
            FWXMLConfigParser parser(g);
            parser.parse();
            parser.config()->swap(destination);
        }   
    }

    FWConfiguration curr;
    m_cfgMng->to(curr);

    FWConfiguration::KeyValues* cur_kv = (FWConfiguration::KeyValues*)m_origConfig.keyValues();
    FWConfiguration::KeyValues* old_kv = (FWConfiguration::KeyValues*)destination.keyValues();

    for (auto i = m_entries.begin(); i != m_entries.end(); i++) {    
        if ((*i)->IsOn()) {
            std::string key =  nmm.realName((*i)->GetText()->GetString());
            printf("ON check key %s\n", key.c_str());
            for(FWConfiguration::KeyValues::iterator it = cur_kv->begin(); it != cur_kv->end(); ++it)
            {
                if ( key.compare(it->first) == 0) {
                    // we found it in current config, now check if we have to add or replace it in old config
                    bool replace = false;
                    {
                        for(FWConfiguration::KeyValuesIt t = it->second.keyValues()->begin(); t != it->second.keyValues()->end(); ++t)
                            printf("CURRENT subentry %s \n", t->first.c_str());
                    }
                    if (old_kv) {
                    for(FWConfiguration::KeyValues::iterator oldit = old_kv->begin(); oldit != old_kv->end(); ++oldit) {
                        printf("compare with the entries \n");
                        if ( key.compare(oldit->first) == 0) {
                            replace = true;
                            printf("REPLACING KEY \n");
                            oldit->second.swap(it->second);
                            {
                                for(FWConfiguration::KeyValuesIt t = oldit->second.keyValues()->begin(); t != oldit->second.keyValues()->end(); ++t)
                                    printf("OLD subentry %s \n", t->first.c_str());
                            }
                            break;
                        }
                    }
                    }
                    printf("endloop\n");

                    if (!replace) {
                        printf("adding new key\n");
                        destination.addKeyValue(it->first, it->second);
                    }

                    break;
                }
            }
        } 
    }

    // Dump content in the file

    std::ofstream file(m_outFileName.c_str());
      if(not file) {
          printf("can't open output file \n");
         return;
      }  
      printf("stream config.....\n");
      FWConfiguration::streamTo(file, destination, "top");

      UnmapWindow();
}
