# Projet CTLV : Task Planner

* Groupe B11 
* Bastien Bigué, Thibaut Sarion.


Afin de répondre à la Task 4 du TP 3, nous avons choisi de développer une application MCV d'agenda très simplifiée. 

Nous avons implémenté cette application avec Django et nous l'avons déployée sous Proxmox, sur le serveur srv-px5. 


## Fonctionnalités

* Gestion d'utilisateurs via un système d'authentification.
* Ajout de tâches à l'agenda.
* Enoncé oral de la tâche ( [Module](https://github.com/pndurette/gTTS) Python client de l'api Text-To-Speech GOOGLE ).
* Suppression automatique de la tâche une fois la date limite dépassée.

## Architecture

![alt text](https://image.ibb.co/kcspsm/Django_App_CTLV.jpg)

Comme énoncé précédemment, notre application a été développée sous Django et déployée sur Proxmox. 

Afin de répondre au mieux à la demande d'architecture en micro-services, nous avons choisi de séparer la base de données du coeur de l'application. Pour cela, nous avons mis en place deux containers Proxmox.

Le premier, ct-tpgei-ctlv-B11-serverDjango, contient l'application web en elle même. Nous avons utilisé le serveur web embarqué par Django.

Le second, ct-tpgei-ctlv-B11-MySqlDB, contient un serveur MySQL. C'est ici que sont donc stockées toutes les informations relatives à notre application web.

Les deux containers appartiennent au même VLAN (2112) afin de pouvoir communiquer entre eux. De plus, le container ct-tpgei-ctlv-B11-serverDjango appartient aussi au VLAN 2028 afin d'être accessible depuis le réseau de l'INSA. 


Résumé : 
Proxmox -> srv-px5 : 
* Container ct-tpgei-ctlv-B11-serverDjango : login : root ; password : thibaut9& ; VLAN : 2028, 2112 ; 
* Container ct-tpgei-ctlv-B11-MySqlDB : login : root ; paassword : thibaut9& ; VLAN : 2112


## Comment l'utiliser ? 

Notre application est accessible via l'adresse : http://10.20.28.156/agenda depuis le réseau INSA

Normalement, les deux serveurs tournent (nous les avons lancé via un screen).

Si le serveur Django venait à ne pas fonctionner, voici comment le relancer : 

* se connecter au réseau de l'INSA
* aller sur proxmox (https://srv-px1.insa-toulouse.fr:8006/)
* ouvrir la console du container ct-tpgei-ctlv-B11-serverDjango sur srv-px5 (login : root ; password : thibaut9&)
* trouver toutes les instances de serveur Django déjà lancées (ps -ef | grep runserver)
* les arrêter (kill -9 pid)
* se déplacer dans le dossier du projet cd /root/SaaSApplication/
* relancer une instance du serveur Django sur le port 80 (python3 manage.py runserver 80)
* accéder à l'application via http://10.20.28.156/agenda


## Perspectives

Nous avions aussi pensé à faire un serveur REST permettant à l'utilisateur de créer une tâche ou de dumper les tâches programmées via des requêtes REST. Nous l'aurions déployée sur un container différent, afin de déployer une architecture en micro-services comme demandé. 