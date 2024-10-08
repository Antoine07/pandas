# Projet RPA factures
## Aperçu du projet
Le projet **RPA factures** est un TP qui a pour but la réalisation d'une application de gestion de factures afin de pouvoir établir le bilan pédagogique et financier d'un organisme de formation.
L'objectif à la fin de ce TP, est la mise en oeuvre d'une API RESTful implémentant des fonctionnalités de récupération de factures selon des critères de sélection et une interface graphique permettant de consommer les données de cette API pour calculer des points importansts de ce bilan pédagoqique et financier.
## Architecture du projet
### Diagramme d'architecture
Le projet RPA est développée sous une architecture dite **n-tiers** plus précisément l'architecture **3-tiers**.

![Schématisation de l'arhitecture 3-tiers](https://blog.lecacheur.com/wp-content/uploads/2017/01/3-tiers-standard.png)

On a une couche présentation responsable des interfaces graphiques et interactions avec les utilisateurs, une couche métier responsable de la logique applicative et une couche de données qui permet l'accés et le stockage des données.
### Technologies utilisées
- **Backend**: Python (FastAPI), Postgres SQL
- **Frontend**: NodeJs, Vite, ReactJs
- **DevOps**: Docker
## Modèle de données
Le projet RPA s'appuie sur le modèle de données suivant:
- **Role** : (id, name)
- **Permission** : (id, action, description)
- **Role_Permission** : (id, role_id, permission_id)
- **User** : (id, email, password, firstname, lastname, role_id)
- **School** : (id, name)
- **Trainer** : (id, name)
- **Subject** : (id, name)
- **Invoice** : (id, invoice_number, issue_date, payment_due, invoice_wording, days_count, hours_count, unit_price, tva, amount_ht, amount_ttc, intervention_dates, workforce, school_id, trainer_id, subject_id)

```mermaid
erDiagram
Role{
    id int pk
    name varchar
}
Permission{
    id int pk
    action varchar
    description varchar
}
Role_Permission{
    id int pk
    role_id int fk
    Permission_id int fk
}
User{
    id int pk
    email varchar
    password varchar
    firstname varchar
    lastname varchar
    role_id int fk
}
School{
    id int pk
    name varchar
}
Trainer{
    id int pk
    name varchar
}
Subject{
    id int pk
    name varchar
}
Invoice{
    id int pk
    invoice_number varchar
    issue_date date
    payment_due varchar
    invoice_wording varchar
    days_count int
    hours_count int
    unit_price float
    tva float
    amount_ht float
    amount_ttc float
    intervention_dates JSONB
    workforce int
    school_id int fk
    trainer_id int fk
    subject int fk
}
Role ||--o{ Role_Permission : "1,n"
Permission ||--o{ Role_Permission : "1,n"
Role ||--o{ User : "1,n"
School ||--o{ Invoice : "1,n"
Trainer ||--o{ Invoice : "1,n"
Subject ||--o{ Invoice : "1,n"
````
**NB**: On considère qu'une facture concerne une école, un formateur et une matière.

## Installation et configuration
### Prérequis
Pour une **installation locale** vous aurez besoin de:
- **Python** 3.9 ou plus ([ressources installation](https://www.python.org/downloads/))
- **PostgresSQL** 16.4 ([ressources installation](https://www.postgresql.org/download/))
- **Node.js** 22 ou plus ([ressources installation](https://nodejs.org/fr))
- Le gestionnaire de dépendances **npm** ou **yarn** installé

Pour une installation via des conteneurs (méthode recommandée pour ce TP) vous aurez juste besoin de **Docker**. ([ressources installation](https://www.docker.com/get-started))
### Installation et configuration du back (Fast API)
Si vous optez pour une installation en local,
- **1-** Cloner le projet
```bash
git clone https://github.com/brightmarc90/rpa_api.git
cd rpa_api
```
- **2-** Créer un environnement virtuel et installer les dépendances
```bash
python -m venv env
source env/bin/activate   # Sur Windows : env\Scripts\activate
pip install -r requirements.txt
```
- **3-** Créer les variables d'environnement

Pour le bon fonctionnement de l'API, vous devez créer la variable d'environnment **`SECRET_KEY`** sur votre système et affectez lui la valeur générée par le code suivant:
```bash
# à exécuter dans un environnement ou fichier python externe au projet
import secrets
print(secrets.token_hex(32))
```
Vous aurez par exemple dans vos variables d'environnement, la clé `SECRET_KEY = your_generated_key`
- **4-** Créer votre base de données

Accéder à votre PostrgreSQL et créez une base de données.
Dans le fichier `alembic.ini` qui se trouve à la racine du projet chercher la ligne suivante et modifiez là avec vos données de connexion:

`sqlalchemy.url = postgresql://user:password@db/nom_db`

avec:
- **user**: étant votre nom d'utilisateur Postgres
- **password**: étant votre mot de passe
- **nom_db**: étant le nom de la base de données que vous avez créé

Faites la même chose pour le fichier `database.py` qui se trouve dans le dossier `api` sur la ligne 

`SQLALCHEMY_DATABASE_URL = "postgresql://user:password@db/nom_db"`

- **5-** Lancer les migrations et le peuplement de la base
```bash
# à la racine du projet
alembic upgrade head
python -m api.seeders.accounts_seeder
python -m api.seeders.invoices_seeder
```
- **6-** Lancer le serveur
```bash
uvicorn main:app --reload
````
Vous devriez avoir accès à l'api sur le `http://localhost:8000`.
Accéder à la documentation de l'API avec des interfaces de test des endpoints sur le `http://localhost:8000/docs`.

Pour démarrer le projet avec Docker rendez-vous dans la section ***Exécution et déploiement***
### Installation et configuration du front (React ViteJS)
Si vous optez pour une installation en local,
- **1-** Cloner le projet
```bash
git clone https://github.com/brightmarc90/rpa_client.git
cd rpa_client
```
- **2-** Installer les dépendances
```bash
npm install
```
- **3-** Créer les variables d'environnement

Dupliquez le fichier `.env.example` qui se trouve à la racine du projet et renommez fichier dupliqué en `.env`. Modifier la ligne

`VITE_APP_SERVER_API="http://url_de_l_api"`

en remplacant http://url_de_l_api par l'URL de base de l'API.
- **4-** Lancer le serveur
```bash
npm run dev
```
Vous devriez avoir accès à l'application sur le `http://localhost:3000` .
## Développement et structure du projet
### Structure du backend
```
- rpa_api/
    - alembic/ 
        - versions/ # dossier des differentes versions des migrations
        - env.py # environment du gestionnaire des migrations
    - api/
        - crud/ # dossier des fonctions de CRUD
        - models/ # dossier des modèles de données
        - schemas/ # dossier des types et formats de réponse de reqûetes encore appelés serializers
        - seeders/ # dossier des fonctions de peuplement de la BD
        - __init__.py
        - database.py # Fichier de configuration / connexion avec la BD
        - router.py # fichier contenant les endpoints de l'API
    - venv/ # Environnement virtuel d'exzcution des dépedances du projet
    - __init__.py
    - .gitignore
    - alembic.ini # fichier de configuration d'alembic
    - Dockerfile # instructions de déploiement sur Docker
    - LICENCE
    - main.py # point d'entrée principal de l'API
    - README.md
    - requirements # liste des dépendances du projet
```
### Structure du frontend
```
- rpa_client/
    - node_modules/ # dépendances du projet
    - public/
    - src/
        - assets/ # dossiers de ressources du projet
        - components/ # dossier des différents composants
        - router/ # contient le ficier de routage de l'appli
        - services/ # dossier des fonctions des requêtes vers l'API
        - views/ # dossiier des différentes vues ou pages 
        - App.css 
        - App.jsx # fichier du composant App qui englobe le reste des composants
        - index.css
        - main.jsx # fichier principal, point d'entrée du projet
    - .env  # fichier des varaibles d'environnement
    - .gitignore 
    - Dockerfile # instructions de déploiement sur Docker
    - index.html 
    - LICENCE
    - package-lock.json
    - package.json # fichier de description des dépendances du projet
    - README.md
```
## Déploiement et exécution
### Contenariser avec Docker
- **1-** Cloner les 2 projets front et back dans un même dossier

Vous devez avoir finalement cette arborescence

```
- Votre_dossier/
    - rpa_api/
    _ rpa_client/
```
- **2-** Configuration
Télécharger les fichier `docker-compose.yml` et `env.example` se trouvant à à [l'adresse-ci](https://github.com/brightmarc90/stage_rpa/blob/main/.env.example) à la racine de votre dossier .

Renommer le fichier `env.example` en `.env` et modifier son contenu en suivant les mêmes étapes qu'à **l'étape 3** de l'installation de l'API sauf qu'ici le token généré par le code sera directement mis dans le fichier `.env`.
- **3-** Construction et démarrage des conteneurs
```bash
docker-compose up --build
docker ps # liste des conteneurs démarrés
```
Un fois les conteneurs démarrés vous dvriez avoir accès à l'API sur le `http://localhost:8000` et à l'appplication front sur le `http://localhost:3000`

- **4-** Lancer les migrations et le peuplement de la base
```bash
# à la racine du projet
alembic upgrade head
python -m api.seeders.accounts_seeder
python -m api.seeders.invoices_seeder
```
### Interaction entre back et front
L'utilisation de l'application est sécurisée par une authentification. Par défaut un super utilisateur est créé et vous pouvez vous connecter avec:
- email : **admin@hae.com**
- mot de passe: **pa$$word**

#### *Comment ça marche ?*
comme dit au début de cette application fontionne sur l'architecture 3-tiers.
- **Le frontend** qui représente la couche **présentation** envoie des requêtes HTTP (POST, GET, PUT, DELETE) à l'API backend pour récupérer ou mettre à jour des données
- **L'API backend** qui représente la couche **métier** traite ces requêtes en appliquant la logique métier et en communiquant avec la base de données pour récupérer ou modifier les données
- **La base de données** qui représente la couche **accès aux données** exécute les opérations de stockage ou de récupération demandées par l'API.
## Licence
Les 2 projets sont sous licence MIT.
## Conclusion
En suivant ce tutoriel, vous avez appris à développer une application web full stack avec un backend en FastPAI (Python) utilisant FastAPI et un frontend en React utilisant ViteJS. Vous avez configuré votre environnement, installé les dépendances, développé l'application, et mis en place le déploiement.
## Ressources supplémentaires
- [Documentation FastAPI](https://fastapi.tiangolo.com/)
- [Documentation React](https://reactjs.org/)
- [Documentation Vite](https://vitejs.dev/)