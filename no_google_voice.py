import appdaemon.plugins.hass.hassapi as hass
import google_voice_text_no as voice_text

class googlevoice(hass.Hass):

  def initialize(self):
      self.register_endpoint(self.api_call)

  def api_call(self, data):
      intent = self.get_dialogflow_intent(data)

      if intent is None:
          self.log("Dialogflow error encountered: Reult is empty")
          return "", 201

      intents = {
           "WelcomeIntent": self.WelcomeIntent,
           "test": self.test,
           "endprompt": self.endprompt,
      }

      if intent in intents:
          speech = intents[intent](data)
          response = self.format_dialogflow_response(speech)
          self.log("Received Dialogflow request: {}, answering: {}".format(intent, speech))
      else:
          response = self.format_dialogflow_response(speech = "I'm sorry, the {} does not exist within AppDaemon".format(intent))
		  
      return response, 200

  def WelcomeIntent(self, data):
      response = voice_text.handleLaunchText()
      return response

  def test(self, data):
      response = "This is a test"
      return response

  def endprompt(self, data):
      response = voice_text.handleCancelText()
      return response

  def get_dialogflow_intent(self, data):
      if "queryResult" in data and "action" in data["queryResult"]:
          return data["queryResult"]["action"]
      else:
          return None

  def get_dialogflow_slot_value(data, slot=None):
      if "queryResult" in data:
            # using V2 API
         contexts = data["queryResult"]["outputContexts"][0]
         if contexts:
             parameters = contexts.get("parameters")
         else:
		     parameters = data["queryResult"]["parameters"]
			 
        if slot is None:
             return parameters
         elif slot in parameters:
             return parameters[slot]
         else:
             return None
      else:
          return None

  def format_dialogflow_response(self, speech=None):
      speech = \
         {
            "fulfillmentText": speech,
            "source": "Appdaemon"
         }

      return speech