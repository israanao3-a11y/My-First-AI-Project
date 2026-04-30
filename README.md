# 🌿 Plant Health Analyzer (AI Vision)

Ce projet utilise l'**Intelligence Artificielle** et la **Vision par Ordinateur** pour analyser la santé des feuilles de plantes et détecter automatiquement les anomalies ou les maladies.

---

## 🎯 Objectif
L'objectif est de simuler la "vision" d'une IA capable d'identifier des motifs anormaux sur une plante en convertissant les images en données numériques exploitables pour un diagnostic rapide.

---

## 🛠️ Fonctionnement Technique

Le programme traite l'image à travers 3 étapes clés de la bibliothèque **OpenCV** :
1.  **Prétraitement** : Conversion de l'image en **niveaux de gris** (Grayscale) pour simplifier l'analyse des textures.
2.  **Segmentation (Thresholding)** : Isolation des taches ou des zones infectées en filtrant les niveaux de luminosité.
3.  **Vision IA** : Génération d'un masque binaire permettant de faire ressortir clairement les zones de stress sur la feuille.

---

## 📊 Technologies Utilisées
* **Python 3.x** : Langage principal.
* **OpenCV** : La bibliothèque référence mondiale pour le traitement d'images.
* **NumPy** : Pour le calcul matriciel haute performance des pixels.

---

## 🚀 Installation et Test
1. Assurez-vous d'avoir une image nommée `leaf.jpg` dans le dossier du projet.
2. Installez les dépendances :
   ```bash
   pip install opencv-python numpy
