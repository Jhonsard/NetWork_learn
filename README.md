# Automatisation Réseau avec Python

**Date de création :** 05/02/2026 - 00h00  
**Date de révision :** 10/02/2026 - 01h00

## 📋 Vue d'ensemble

Ce projet explore **l'automatisation des infrastructures réseau avec Python** pour assurer une gestion proactive, optimale et une disponibilité continue.

L'automatisation réseau représente une **transformation profonde** de la manière de :
- Concevoir les infrastructures
- Déployer les services
- Maintenir les équipements

---

## 🎯 Étapes d'automatisation

### **Étape 1 : Configuration et déploiement des périphériques**
Réduire les erreurs et les temps de configuration manuelle

### **Étape 2 : Surveillance et analyse de réseau**
Monitoring continu de l'infrastructure

### **Étape 3 : Dépannage des incidents**
Résolution automatisée des problèmes

### **Étape 4 : Automatisation de la sauvegarde et des configurations**
Déploiement et comparaison des configurations réseau

### **Étape 5 : Orchestration des réseaux**
Gestion globale et coordonnée de l'infrastructure

---

## ✅ Avantages de l'automatisation

- ✨ Amélioration de l'efficacité et de la productivité des administrateurs réseau
- 🛡️ Réduction des erreurs humaines
- 👁️ Amélioration de la visibilité et du contrôle
- ⚡ Augmentation de l'agilité de l'entreprise
- 💰 Réduction des coûts d'exploitation du réseau

---

## 🐍 Pourquoi Python ?

Python a été choisi pour ce projet car :
- **Facilité** : syntaxe claire et lisible
- **Polyvalence** : large écosystème de bibliothèques réseau
- **Productivité** : développement rapide et efficace

---

## 🚀 Installation préalable

⚠️ **Très important** : Créer un environnement virtuel pour le projet

```bash
# Créer l'environnement
python3 -m venv .venv

# Activer l'environnement
source .venv/bin/activate
```

---

## 📚 Concepts fondamentaux

### 1️⃣ Variables Binaires et Octets

#### Déclaration

```python
variable = bin(10)           # Retourne la représentation binaire de 10
byteu = 0b1010               # Le nombre 10 en binaire (préfixe 0b)

# Les lettres peuvent aussi être en octets
chaine_byte = b"Bonjour"     # Chaîne en octets
chaine_encode = "Bonjour".encode()  # Encoding avec .encode()
```

#### Conversion d'octet en décimal

```python
int('1010', 2)  # Convertit "1010" (base 2) en décimal = 10
```

---

### 2️⃣ Opérations sur les binaires

#### Opérateurs logiques

| Opérateur | Symbole | Description |
|-----------|---------|-------------|
| AND | `&` | ET logique |
| OR | `\|` | OU logique |
| XOR | `^` | OU exclusif |
| NOT | `~` | Complémentaire à 2 |
| Décalage droit | `>>` | Division par 2 |
| Décalage gauche | `<<` | Multiplication par 2 |

#### Exemples d'opérations

**AND (&) :**
```python
0b1010 & 0b1100 = 0b1000  # Résultat : 8
# Explication : 1&1=1, 0&1=0, 1&0=0, 0&0=0
```

**Complémentaire à 2 (NOT ~) :**
```python
~byteu = -(byteu + 1)  # Pour byteu=10 : ~10 = -11
```

**Décalages :**
```python
10 >> 1  # Division par 2 = 5
10 >> 2  # Division par 4 = 2
5 << 1   # Multiplication par 2 = 10
5 << 2   # Multiplication par 4 = 20
```

**Importance :** Ces opérations permettent une manipulation fine des données binaires, notamment pour la gestion des adresses IP et la construction des paquets.

---

### 3️⃣ Conversion d'adresse IP en binaire

#### De décimal à binaire

```python
ip_addr = "192.168.1.13"

# Étape 1 : Découper en octets
octets = ip_addr.split(".")  # ['192', '168', '1', '13']

# Étape 2 : Convertir chaque octet en binaire (8 bits)
binary_array = []
for octet in octets:
    binary_array.append(format(int(octet), '08b'))

# Étape 3 : Joindre en une seule chaîne
ip_bin = ''.join(binary_array)
# Résultat : '11000000101010000000000100001101'
```

#### De binaire à décimal

```python
# Étape 1 : Découper la chaîne binaire en octets (8 bits)
octets_renv_list = []
octets_renv_list.append(ip_bin[0:8])
octets_renv_list.append(ip_bin[8:16])
octets_renv_list.append(ip_bin[16:24])
octets_renv_list.append(ip_bin[24:32])

# Étape 2 : Convertir chaque octet binaire en décimal
for i in range(4):
    octets_renv_list[i] = str(int(octets_renv_list[i], 2))

# Étape 3 : Joindre avec des points
ip_renv = '.'.join(octets_renv_list)
# Résultat : '192.168.1.13'
```

**Remarque importante :** L'adresse IP publique est l'inverse du code binaire de l'adresse IP privée.

---

## 🏗️ Programmation Orientée Objet (POO)

### 1. Types d'attributs et de méthodes

#### **Variables d'instance**
- Accessibles après instanciation
- Syntaxe : `self.variable`
- Méthodes d'instance : prennent `self` en paramètre

#### **Variables de classe**
- Liées uniquement à la classe
- Accessibles : `NomClasse.variable_classe`
- Méthodes de classe : décorées avec `@classmethod` et prennent `cls`

```python
@classmethod
def methode_classe(cls):
    pass
```

#### **Variables statiques**
- Indépendantes de la classe et des instances
- Décorées avec `@staticmethod`
- Accessibles : `NomClasse.methode_statique()`

```python
@staticmethod
def methode_statique():
    pass
```

---

### 2. Encapsulation

Restriction de l'accessibilité aux données de la classe :

| Type | Syntaxe | Accès |
|------|---------|-------|
| Public | `self.variable` | Partout |
| Protected | `self._variable` | Classe et héritage |
| Private | `self.__variable` | Classe uniquement |

```python
class Utilisateur:
    def __init__(self, nom):
        self.nom = nom              # Public
        self._email = None          # Protected
        self.__password = None      # Private
```

---

### 3. Composition vs Héritage

La **composition** permet d'intégrer d'autres classes pour plus de flexibilité :

```python
class AddressIP:
    def __init__(self, ip):
        self.ip = ip

class Utilisateur:
    def __init__(self, nom: str, ip: str, status: bool):
        self.nom = nom
        self.ip = AddressIP(ip)     # Composition
        self.status = status

# Accès : utilisateur.ip.ip (deux fois la variable)
```

---

### 4. Méthodes magiques et surcharge d'opérateurs

Les méthodes magiques (délimitées par `__`) redéfinissent le comportement des objets :

#### **Principales méthodes magiques**

| Méthode | Usage |
|---------|-------|
| `__init__` | Constructeur |
| `__str__` | Représentation pour `print()` |
| `__repr__` | Représentation détaillée |
| `__eq__` | Comparaison d'égalité (`==`) |
| `__lt__`, `__gt__` | Comparaisons (`<`, `>`) |
| `__del__` | Destructeur |

#### **Exemple : classe IPAddress**

```python
class IPAddress:
    def __init__(self, ip):
        self.ip = ip

    def __str__(self):
        return f"IP Address : {self.ip}"
    
    def __repr__(self):
        return f"IPAddress('{self.ip}')"
    
    def __eq__(self, other):
        return self.ip == other.ip
    
    def __lt__(self, other):
        """Compare deux adresses IP"""
        return self.convertir_en_int() < other.convertir_en_int()
    
    def convertir_en_int(self):
        """Convertit l'IP en entier"""
        octets = map(int, self.ip.split("."))
        return (next(octets) << 24) + (next(octets) << 16) + \
               (next(octets) << 8) + next(octets)

# Utilisation
ip1 = IPAddress("192.168.10.1")
ip2 = IPAddress("192.168.1.1")
ip3 = IPAddress("192.168.1.1")

print(ip1)                    # IP Address : 192.168.10.1
print(repr(ip2))              # IPAddress('192.168.1.1')
print(ip2 == ip3)             # True
print(ip1 > ip2)              # True
print(ip1 < ip3)              # False
```

---

### 5. Classes abstraites

Les classes abstraites définissent une interface que les classes filles doivent implémenter :

```python
from abc import ABC, abstractmethod

class DispositifSecurite(ABC):
    """Classe abstraite pour les dispositifs de sécurité réseau"""
    
    def __init__(self, nom):
        self.nom = nom
    
    @abstractmethod
    def activer(self):
        """Méthode abstraite : doit être implémentée"""
        pass
    
    @abstractmethod
    def desactiver(self):
        """Méthode abstraite : doit être implémentée"""
        pass
    
    def afficher_nom(self):
        """Méthode concrète"""
        return f"Dispositif de sécurité : {self.nom}"

class Parefeu(DispositifSecurite):
    def activer(self):
        return f"{self.nom} est activé"
    
    def desactiver(self):
        return f"{self.nom} est désactivé"

class IDS(DispositifSecurite):
    def activer(self):
        return f"L'IDS {self.nom} est activé"
    
    def desactiver(self):
        return f"L'IDS {self.nom} est désactivé"

# Utilisation
parefeu = Parefeu("Cisco_01")
ids = IDS("Snort_1024")

print(parefeu.afficher_nom())        # Dispositif de sécurité : Cisco_01
print(parefeu.activer())             # Cisco_01 est activé
print(ids.desactiver())              # L'IDS Snort_1024 est désactivé
```

---

### 6. Interfaces

Une interface est une classe abstraite contenant **uniquement des méthodes abstraites** :

```python
from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def authentifier(self, user, password):
        pass

class AuthentificationLDAP(Interface):
    def authentifier(self, user, password):
        print(f"Authentification LDAP pour {user}")

class AuthentificationAD(Interface):
    def authentifier(self, user, password):
        print(f"Authentification Active Directory pour {user}")
```

---

### 7. Héritage multiple

⚠️ Attention : l'héritage multiple peut causer des conflits.

#### **Problème du diamant**

```python
class A:
    def action(self):
        print("Action A")

class B(A):
    def action(self):
        print("Action B")

class C(A):
    def action(self):
        print("Action C")

class D(B, C):
    def action(self):
        print("Action D")

d = D()
d.action()  # Résultat : "Action B" (suit la MRO)
```

#### **Résolution : utiliser `super()` ou appeler explicitement**

```python
class D(B, C):
    def action(self):
        B.action(self)
        C.action(self)
        print("Action D")

d = D()
d.action()  # Affiche : Action B, Action C, Action D
```

#### **Exemple pratique**

```python
class SecurityParefeu:
    def filtrer_ip(self):
        print("Filtrage des IPs en cours")

class DetectionIntrusion:
    def detecter_intrusion(self):
        print("Détection d'intrusion en cours")

class ParefeuAvanc(SecurityParefeu, DetectionIntrusion):
    pass

parefeu = ParefeuAvanc()
parefeu.filtrer_ip()              # Filtrage des IPs en cours
parefeu.detecter_intrusion()      # Détection d'intrusion en cours
```

**Avantage :** Gérer plusieurs classes parents et leurs fonctionnalités simultanément.

---

### 8. Décorateurs

Les décorateurs modifient le comportement d'une fonction ou méthode :

```python
def valider_entree(fonction):
    """Décorateur de validation des entrées"""
    def nouvelle_action(self, *args, **kwargs):
        if any(arg < 0 for arg in args):
            print("❌ Les arguments ne peuvent pas être négatifs")
            return None
        return fonction(self, *args, **kwargs)
    return nouvelle_action

class Calculatrice:
    @valider_entree
    def additionner(self, a, b):
        return a + b
    
    @valider_entree
    def soustraire(self, a, b):
        return a - b

machine = Calculatrice()
print(machine.additionner(5, 10))      # 15
print(machine.additionner(-1, 12))     # ❌ Les arguments ne peuvent pas être négatifs
print(machine.soustraire(20, 5))       # 15
```

---

### 9. Mixins

Les **mixins** sont des classes qui ajoutent des fonctionnalités à d'autres classes via l'héritage multiple :

```python
class JournalisationMixin:
    """Mixin pour ajouter la journalisation"""
    def journaliser(self, message):
        print(f"[JOURNAL] {message}")

class Parefeu:
    def filtrer_paquets(self):
        print("Filtrage des paquets en cours")

class ParefeuJournalise(Parefeu, JournalisationMixin):
    def filtrer_paquets(self):
        self.journaliser("Début du filtrage des paquets")
        super().filtrer_paquets()
        self.journaliser("Filtrage des paquets terminé")

journal = ParefeuJournalise()
journal.filtrer_paquets()

# Résultat :
# [JOURNAL] Début du filtrage des paquets
# Filtrage des paquets en cours
# [JOURNAL] Filtrage des paquets terminé
```

**Utilisations possibles :** chiffrage, logging, authentification, etc.

---

### 10. Slots (`__slots__`)

Les slots réduisent la consommation mémoire en limitant les attributs possibles :

```python
class Utilisateur:
    __slots__ = ["nom", "age"]
    
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

user = Utilisateur("Alice", 30)
# user.email = "alice@example.com"  # ❌ AttributeError : 'Utilisateur' objet n'a pas d'attribut 'email'
```

---

## 📝 Résumé des concepts

| Concept | Utilité | Exemple |
|---------|---------|---------|
| **Encapsulation** | Sécuriser les données | `self._private` |
| **Composition** | Intégrer des objets | `self.ip = IPAddress()` |
| **Classes abstraites** | Définir une interface | `@abstractmethod` |
| **Décorateurs** | Modifier les fonctions | `@classmethod`, `@staticmethod` |
| **Mixins** | Ajouter des fonctionnalités | `JournalisationMixin` |
| **Héritage multiple** | Combiner plusieurs classes | `class D(B, C):` |
| **Slots** | Économiser la mémoire | `__slots__ = ["attr1"]` |

---

## 📌 Prochaines étapes

- [ ] Implémenter les classes de gestion réseau
- [ ] Développer les modules de surveillance
- [ ] Créer l'API d'orchestration
- [ ] Écrire les tests unitaires
- [ ] Documenter les cas d'usage en détail

---

**Auteur :** TFCProject  
**Licence :** À définir  
**Version :** 1.0.0
