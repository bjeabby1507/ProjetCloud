# Projet Cloud

## Introduction
L’objectif est de mettre en place une solution logicielle complète permettant de  collecter des événements d’une source de données (produisant potentiellement beaucoup de données), d’appliquer à ces données des fonctions de traitement, et de  stocker ces données afin des fins de piste d’audit.

## Étapes
Nous utiliserons les services Azure :

- Etape 1 : Identifier une source de données
  - **Nownodes** : 20 000 requêtes par jour, donne accès à plusieurs réseaux Blockchain
- Etape 2 : collecte des données
  - **Script python**
- Etape 3 : Envoyer les données vers un hub de données
  - **Azure Hubs** : collecteur de données sous forme d’événements.
- Etape 4 : Développement d’un module logiciel de traitement des données
  - **Azure** **Function** :
- Etape 5 : Stockage des données
  - **Azure Blob Storage** : 
- ​	Étape 6 : Gestion des cas aux limites

