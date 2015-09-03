import datetime
import dateutil.parser
import mandrill
import re
import time


class MandrillCommunicationService:
  """
  An implementation of the communication service interface using Mandrill.
  """
  def templateType(self):
    return "MANDRILL"

  def initialize(self, config):
    # Save all config details.
    self.api_key = config.get("MANDRILL_API_KEY")
    self.update_interval_seconds = int(config.get(
        "MANDRILL_UPDATE_INTERVAL_SECONDS", 0))

    # Initialize Mandrill from the details.
    self.mandrill = mandrill.Mandrill(self.api_key)

    # Perform the first update of the CommunicationTemplates.
    self.last_update_time = None


  def send(self, from_email, to_email, subject, message):
    # Create the subaccount for this communication if necessary, and get the ID.

    # Create the Mandrill message.
    # For details on available Mandrill parameters see:
    # https://mandrillapp.com/api/docs/messages.python.html
    # TODO: Add signing domain here when we have one.
    message = {
      "from_email": from_email,
      "from_name": from_email,
      "to": [{
        "email": to_email,
        "name": to_email,
        "type": "to",
      }],
      "subject": subject,
      "text": message,
      "inline_css": True,
      "url_strip_qs": False,
      "view_content_link": True,
    }


    # Send the communication.
    try:
      result = self.mandrill.messages.send(
            message=message,
            async=False,
            ip_pool=None,  # No dedicated IP pool.
            send_at=None)  # Send immediately.
    except mandrill.Error, e:
      # Mandrill errors are thrown as exceptions.
      print "A mandrill error occurred: %s - %s" % (e.__class__, e)
      raise

    # Store the send details even when there's an error.
    result = result[0]

    return result

