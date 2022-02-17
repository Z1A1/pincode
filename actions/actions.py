# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from matplotlib.pyplot import text
from api import Pin

import requests
import json 
from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet,FollowupAction
from rasa_sdk.forms import FormAction


from rasa_sdk import Action, Tracker,FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk.executor import CollectingDispatcher
import requests
#
#

class Actionsubmit(Action):
    def name(self) -> Text:

      return "action_validate"
    def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
      
       
      mess=tracker.get_slot("pincode") 
     
      input=tracker.get_slot("loc")
      Pin(mess,input)
      r=Pin.k 
      
      dispatcher.utter_message(text=f"your {input} is {r}")
      
      return ()
       

        


    
    


        
#
         
#
