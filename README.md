# robotai
features:
- speech->text->LLM (self hosted/openai/lemur w/ assemblyai/ or other options) + way to parse commands -> speech (speakers) or homeassistant commands
- has servo and leds to move and light up
- mongodb will be used to store conversations for each day (ideally this could be used in the future?) and then stored somewhere else for long term storage
- leds and motor will correspond to certain commands or loading times or other similary things
- home assistant will be configured on home server and will be fed commands from robot
- tbd
=============================================================================
progress:
- voice> whisper locally works, sr seems to added more errors--> need to suppress w/ some alsa config edits, takes very long, not real time at all, not sure how to do this without ML workstation or just using a api and figuring out how to split commands and questions
- servos/leds> work good need to try on actual chassis and implement gpio extender
