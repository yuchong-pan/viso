# viso
Viso project by hack.init() at HackNanjing

## Features
Currently, Viso has the following fully-functional features both from web platform side and the Leap Motion side.

### Web Platform Server
1. An integrated UI of video calls, text messaging and synchronous online editor.
2. Alerting system for anti-cheating.
3. Standardized API endpoints for sending alerts from Leap Motion (and potential extensible hardware devices).

### Leap Motion
1. Monitor hand positions of interviewees and retrieve data from Leap Motion.
2. Send alerts to web server via HTTP requests.

## Techonology

### Web Platform Server

#### Front-End
1. **LeanCloud API** -- for text messaging and video calls
2. **Ace Online Editor** -- An easy-to-use online editor, used by various websites like GitHub

#### Back-End
1. **Flask Web Framework** -- to transfer alerts from Leap Motion to the front-end
2. **WebSocket** -- to send alerts from the back-end to front-end
3. **Docker** -- to standardized the environment and encapsulate services
4. **Nginx** -- to serve as reverse proxy

### Leap Motion
1. **Python** -- to send alerts to the web server when anomalies are detected

## Copyright
Copyright © Yuchong PAN, Shaolin ZHANG, Yiluo LI. All Rights Reserved.
This project is created at HackNanjing in 2017.
