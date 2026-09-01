::: titlepage
**TOM+ User Manual**

Version 2.0

![image](figures/tom_plus.png){width="85%" height="70%"}

Fabio Java

2026
:::

# Préface {#préface .unnumbered}

*Ceci est le manuel d'utilisation officiel de ToM+ rédigé à la main par moi-même (Fabio Java) en anglais, sans utiliser aucun outil d'IA, ni dans ce guide ni dans le code qui fait fonctionner ToM+. Les langues autres que l'anglais ont été traduites automatiquement à l'aide de* [DeepL](https://www.deepl.com/en/translator).\
*À une époque de génération automatisée de contenu, ce manuel se distingue et vous pouvez être certain que toutes les fonctionnalités et l'interface utilisateur fournies sont écrites par un humain. C'est ce qui rend ce projet unique parmi toutes les alternatives : savoir exactement ce que fait le code est la clé pour développer consciemment de nouvelles fonctionnalités, corriger les bugs et garantir un support aux autres propriétaires de ToM+ si nécessaire.*\
*ToM+ évolue constamment avec l'aide de sa grande communauté née du* [forum allemand Twizy](https://www.twizy-forum.de/twiz-o-meter). *Si vous souhaitez obtenir une unité ToM+, envoyez-moi un e-mail à* **info.twizometer@gmail.com**. *Si vous souhaitez suggérer une nouvelle fonctionnalité, signaler un bug ou même une faute de frappe dans ce manuel, veuillez m'envoyer un e-mail ou ouvrir une pull request sur* [Codeberg](https://codeberg.org/fabio-java/ToM-Wizard).\
*Si vous possédez un ToM standard ou un BigToM, vous pouvez également vous référer à ce manuel d'utilisation, car les fonctionnalités sont essentiellement les mêmes, à l'exception du ToM standard où la page du tableau de bord et les pages de charge 3D sont absentes.*\
*Ce manuel d'utilisation est mis à jour pour la version 2.4 du micrologiciel ESP.*

# Description et liste des fonctionnalités

## Points forts des fonctionnalités du ToM+

Le ToM+ possède de nombreuses fonctions et peut être constamment mis à jour au fil du développement du micrologiciel. Dans les paragraphes suivants, je vais vous donner une brève introduction de ses fonctionnalités, afin de vous donner une idée du type de produit que j'expliquerai plus en détail ultérieurement dans le manuel.

### Un nouveau tableau de bord pour Twizy

Puisque le tableau de bord de notre Twizy n'inclut que quelques valeurs, comme la vitesse et les kilomètres restants, j'ai décidé de développer cet affichage élégant qui montrera beaucoup plus de données, en les lisant directement depuis le bus CAN de la Twizy à l'aide du connecteur OBD situé dans la boîte à gants gauche. Le ToM va simplement « écouter » les valeurs envoyées par la Twizy puis les afficher sur l'écran LCD, permettant ainsi de nombreuses autres fonctionnalités. Le ToM dispose d'une mémoire petite mais puissante capable de stocker certaines de ces valeurs pendant la conduite afin de vous fournir un historique des trajets. Sa capacité à stocker certaines valeurs permet de sauvegarder vos configurations et personnalisations sur le ToM, même après une mise à jour du micrologiciel.

<figure data-latex-placement="H">
<img src="figures/dashboard.jpg" style="width:80.0%" />
<figcaption>Tableau de bord du ToM+</figcaption>
</figure>

Il tente de conserver le même style que le tableau de bord d'origine de la Twizy, mais avec un look 3D plus moderne. Comme sur l'original, vous retrouvez la batterie, la vitesse engagée, les kilomètres restants, la vitesse et l'heure. Mais j'ai ajouté le **pourcentage exact de la batterie**, le couple moteur, des icônes d'état, des informations sur le trajet et plein d'autres éléments que vous pouvez configurer selon vos souhaits et que nous verrons en détail plus tard.

La page principale est personnalisable et vous pouvez choisir ce que vous souhaitez y afficher, tout comme les autres pages que vous pouvez faire défiler à l'aide du bouton à monter sur la commande d'essuie-glace. L'aspect général des autres pages est présenté sur l'image, avec une valeur au premier plan et les autres sur le côté gauche. En bas, vous pouvez changer la page affichée en appuyant sur son icône.

<figure data-latex-placement="H">
<img src="figures/engine_page.jpg" style="width:80.0%" />
<figcaption>Page moteur du ToM+</figcaption>
</figure>

### Connectivité WiFi

La carte ESP32 contenue dans le boîtier noir a la capacité de se connecter à un point d'accès réseau WiFi. Une fois le ToM+ connecté, vous pouvez faire plein de choses. Par exemple, cet appareil peut être utilisé pour transférer des données de votre Twizy vers votre broker **MQTT** personnel, où vous pouvez utiliser ces valeurs pour intégrer votre voiture dans votre système domotique IoT.

Ce n'est pas la seule fonctionnalité liée au Wi-Fi du ToM+. Il est également capable de fonctionner en tant que point d'accès avec son propre SSID et mot de passe, créant ainsi un réseau privé sans connexion Internet. De cette façon, vous pouvez vous connecter en toute sécurité, **en acceptant de maintenir le profil de connexion actif** même s'il ne fournit pas de connexion Internet (cela apparaît généralement sous forme de notification sur les téléphones Android 10 secondes après la première connexion), puis effectuer vos configurations supplémentaires sur des pages Web hébergées par le ToM+ lui-même. Tapez simplement l'IPv4 privée statique du ToM (***192.188.1.188***) dans votre navigateur préféré et profitez-en !

<figure data-latex-placement="H">
<img src="figures/landing_page.png" style="height:75.0%" />
<figcaption>Page d’accueil du serveur web</figcaption>
</figure>

Comme vous pouvez le voir dans cette nouvelle version de ToM, le serveur web est beaucoup plus complet et convivial. Vous pouvez facilement naviguer à travers les pages et configurer votre appareil comme vous le souhaitez. Le serveur web est également réactif (responsive), vous pouvez donc l'utiliser aussi bien sur votre smartphone que sur votre tablette.

### Application smartphone ToM

Parallèlement aux mises à jour du micrologiciel de l'écran LCD et du boîtier noir, une application Android minimale est également tenue à jour et vous permettra de surveiller les données en temps réel de votre Twizy à l'aide de votre smartphone.

La mise en page tente d'émuler l'interface graphique originale de ToM et s'appuie sur le protocole **MQTT** pour partager et transférer les valeurs de ToM+ vers l'application. Vous devrez donc la configurer à la fois sur l'application et sur la page MQTT de ToM+, en inversant les sujets IN et OUT. L'application est distribuée sous forme de fichier **APK**, un installateur d'application pour Android qui vous permet d'installer cette application même sans connexion Internet. Elle est disponible en [cliquant ici](https://www.mediafire.com/file/du7px1bzq0zzdxu/TwizOMeter_v3.1.2.apk/file).

Vous devrez peut-être activer l'option « installer des applications de sources inconnues » dans les paramètres de votre téléphone pour ouvrir cette extension de fichier *(.apk)*. Au premier démarrage, vous remarquerez peut-être un message contextuel indiquant que cette application a été créée pour une version plus ancienne d'Android si vous avez un téléphone plus récent : cliquez simplement sur OK et ignorez-le (elle fonctionnera parfaitement). Voici un aperçu des pages de charge et de paramètres de l'application :

<figure data-latex-placement="H">
<img src="figures/tom_app_charging.png" style="width:80.0%" />
<figcaption>Page de charge de l’application Android ToM+</figcaption>
</figure>

<figure data-latex-placement="H">
<img src="figures/tom_app_settings.png" style="width:65.0%" />
<figcaption>Page des paramètres de l’application Android ToM+</figcaption>
</figure>

### Aperçu rapide de la consommation

ToM utilisera l'alimentation de la batterie 12V, en la prélevant directement sur le connecteur OBD et ne consommera pas beaucoup, comme le montrent les mesures progressives ci-dessous.

<figure data-latex-placement="H">
<img src="figures/consumption_off.png" style="width:65.0%" />
<figcaption>Consommation lorsque la Twizy est éteinte (OFF)</figcaption>
</figure>

Lorsque la carte mère est active et que l'affichage est allumé, il consomme environ 90 mA. Si le WiFi est également activé, la consommation d'énergie est d'environ celle indiquée ci-dessous (peut-être un peu plus en raison des dernières mises à jour qui ont introduit le graphisme 3D).

<figure data-latex-placement="H">
<img src="figures/consumption_on_wifi.png" style="width:65.0%" />
<figcaption>Consommation lorsque le ToM+ est allumé (ON) avec le WiFi</figcaption>
</figure>

Lorsque la Twizy est éteinte (OFF), le boîtier noir passe en mode veille et consomme 18 mA. De plus, la fonctionnalité tactile vous permettra d'interagir beaucoup plus facilement avec l'appareil et son écran LCD. Comme il utilise une technologie tactile résistive, vous pouvez utiliser vos doigts ou un petit stylet en plastique dur pour appuyer sur les boutons. Ce n'est pas aussi puissant que les tableaux de bord à écran tactile capacitif, mais une fois que vous l'aurez essayé, vous ne pourrez plus vous en passer, croyez-moi !

## Kit ToM+ fourni

Lorsque ToM+ est expédié, il est généralement emballé dans une boîte en carton brune afin de protéger les cartes internes et les capteurs contre les chocs pendant le transport. Dans cette version plus récente, aucun long câble n'est nécessaire, seulement un câble plus court connecté à la carte mère interne du ToM+, enfermée dans un petit conteneur en plastique noir que j'appelle habituellement « boîtier noir » (black box). Bien entendu, l'écran tactile LCD résistif est fourni avec, sur lequel vous pouvez tout visualiser et tout configurer. Plus besoin de vis ni de ruban adhésif ! Juste un écran à clipser facilement qui s'adapte directement sur le dessus du tableau de bord d'origine.

<figure data-latex-placement="H">
<img src="figures/box.png" style="width:80.0%" />
<figcaption>Kit ToM+ fourni</figcaption>
</figure>

### Le boîtier noir (Black Box)

Le boîtier noir est la carte mère du ToM+ et contient la plupart des composants nécessaires au fonctionnement du système. Il fournit :

- Un connecteur externe pour l'écran LCD ;

- Un connecteur d'extension avec des broches d'alimentation et GPIO ;

- Un port OBD femelle intégré pour le bus CAN de la Twizy ;

- Un port microUSB pour les mises à jour du micrologiciel ;

- Un connecteur femelle pour le bouton sur la commande d'essuie-glace ;

- Un interrupteur d'alimentation ON/OFF pour le ToM+.

<figure data-latex-placement="H">
<img src="figures/black_box.jpg" style="width:75.0%" />
<figcaption>Le boîtier noir</figcaption>
</figure>

### Le connecteur d'extension

Si vous souhaitez personnaliser davantage votre ToM+, vous pouvez facilement le faire en utilisant le connecteur illustré sur l'image ci-contre. En fait, il fournit une alimentation 5V supplémentaire provenant de VCC (ancien câble rouge) et de GND (ancien câble noir), de sorte que vous puissiez alimenter une LED externe, un petit vibreur/buzzer ou tout ce que vous préférez. Les deux autres câbles sont des broches d'entrée/sortie générales (GPIO), PIN1 (ancien jaune) et PIN2 (ancien bleu). Elles peuvent avoir des fonctions d'entrée ou de sortie, selon ce que vous choisirez sur la *« Page d'extension »* du **serveur web** ToM. Dans cette dernière version de l'appareil, le connecteur d'extension est intégré dans le boîtier noir (sans câbles de couleur) mais le brochage reste le même. N'oubliez pas d'enlever le cache de protection avant de l'utiliser et d'utiliser une tension d'entrée de **maximum 3,3V**. Pour une tension plus élevée, prévoyez un diviseur résistif approprié.

<figure id="fig:expansion_pinout" data-latex-placement="H">
<img src="figures/expansion_bb.jpg" style="width:70.0%" />
<figcaption>Connecteur d’extension</figcaption>
</figure>

### L'écran LCD et son support

L'écran LCD tactile résistif est intégré dans un support imprimé en 3D qui se clips sur le tableau de bord d'origine. Sur demande, vous pouvez également disposer d'un support autonome en 3D pour monter l'écran sur la boîte à gants comme le ToM standard. De cette façon, vous pouvez avoir un appareil 2 en 1 qui peut être soit à clipser, soit autonome selon vos souhaits. Un logement microSD est accessible pour les mises à jour du micrologiciel.

<figure data-latex-placement="H">
<img src="figures/display.png" style="width:80.0%" />
<figcaption>Écran LCD à clipser</figcaption>
</figure>

L'écran, fourni avec un film de protection, comme visible sur les images, peut être placé dans le conteneur 3D pour disposer d'un support réglable que vous pouvez placer où vous le souhaitez.

<figure data-latex-placement="H">
<img src="figures/3d_stand_wdisplay.png" style="width:80.0%" />
<figcaption>Écran LCD autonome</figcaption>
</figure>

Lorsqu'il est placé dans la version autonome, vous pouvez le fixer avec le couvercle et les vis que vous trouverez dans le paquet avec le support pliable 3D, comme le montrent les images ci-dessous.

<figure id="fig:back_cover" data-latex-placement="H">
<img src="figures/back_cover.png" style="width:80.0%" />
<figcaption>Couvercle arrière LCD fourni</figcaption>
</figure>

Le support 3D comporte également des trous sur sa base si vous souhaitez le visser sur la boîte à gants. Les autres trous sur le cadre sont prévus pour visser le couvercle arrière afin de maintenir l'écran en place une fois à l'intérieur.

<figure id="fig:bottom_cover_screwholes" data-latex-placement="H">
<img src="figures/bottom_cover_screwholes.png" style="width:80.0%" />
<figcaption>Fixation par vis du couvercle LCD</figcaption>
</figure>

### Composants utiles supplémentaires

Le paquet comprend un collier de serrage (serre-câble) pour fixer le support imprimé en 3D du bouton sur la commande d'essuie-glace droite (également incluse). De plus, il y a un autocollant en bonus si vous souhaitez soutenir le projet en le collant quelque part sur votre Twizy.

<figure data-latex-placement="H">
<img src="figures/cable_tie.jpg" style="width:80.0%" />
<figcaption>Collier de serrage</figcaption>
</figure>

<figure id="fig:wiper_stalk_button" data-latex-placement="H">
<img src="figures/wiper_stalk_button.jpg" style="width:80.0%" />
<figcaption>Bouton imprimé en 3D pour commande d’essuie-glace</figcaption>
</figure>

<figure data-latex-placement="H">
<img src="figures/sticker.png" style="width:80.0%" />
<figcaption>Autocollant ToM</figcaption>
</figure>

# Installation du Twiz O' Meter sur votre véhicule

L'installation du ToM+ sur votre Twizy est très simple et ne nécessite aucune connaissance particulière car, comme j'ai l'habitude de le dire, c'est un appareil « plug and drive » (prêt à l'emploi) ! Suivez donc ces quelques étapes pour l'installer correctement et rapidement, ou tentez d'essayer par vous-même un autre emplacement.

## Positionnement de l'écran LCD

Lors de la commande de l'appareil, vous pouvez choisir de recevoir le support 3D avec l'écran à clipser. Vous pouvez ainsi choisir d'installer l'écran de deux manières différentes : en utilisant le mode à clipser ou en utilisant le mode support 3D. Le mode à clipser est le plus courant et vous permet de fixer l'écran au tableau de bord de la voiture, tandis que le mode support 3D vous permet de placer l'écran sur une surface plane à l'intérieur du véhicule (je suggère généralement la boîte à gants droite ou gauche).

### Mode à clipser

Si vous choisissez ce mode, c'est très simple. Il vous suffit de clipser l'écran sur le tableau de bord, dans une position confortable à regarder pendant la conduite. Placez la partie supérieure de l'écran sur le tableau de bord, puis poussez la partie inférieure jusqu'à ce qu'elle s'enclenche avec un déclic.

<figure data-latex-placement="H">
<img src="figures/clip_on.jpg" style="width:80.0%" />
<figcaption>Installation en mode à clipser</figcaption>
</figure>

Assurez-vous que le câble n'est pas pincé dans la partie inférieure de l'écran et qu'il est libre de se déplacer dans l'orifice prévu à cet effet, sinon vous risqueriez d'endommager le câble.

### Mode support 3D

S'il est fourni, vous pouvez utiliser le support 3D pour placer l'écran sur une surface plane à l'intérieur de la voiture. Vous pouvez appliquer du ruban adhésif double face en dessous afin de le coller à la surface. Ou vous pouvez utiliser les trous de vis sous le support pour le fixer à l'aide de deux vis.

Comme nous l'avons fait pour le mode à clipser, assurez-vous que le câble n'est pas pincé à l'arrière de l'écran lors de la mise en place du capot, mais qu'il est libre de se déplacer dans l'orifice prévu à cet effet, sinon vous risqueriez d'endommager le câble. Reportez-vous à la Figure [1.2](#fig:back_cover){reference-type="ref" reference="fig:back_cover"} et à la Figure [1.3](#fig:bottom_cover_screwholes){reference-type="ref" reference="fig:bottom_cover_screwholes"} à la page  pour voir les pièces mentionnées. Voici à quoi ressemble le support 3D sans l'écran installé.

<figure data-latex-placement="H">
<img src="figures/3d_stand.jpg" style="width:80.0%" />
<figcaption>Support vide imprimé en 3D</figcaption>
</figure>

### Raccordement du câble

Vous pouvez ensuite retirer le film protecteur de l'écran et brancher le câble pour l'alimenter. L'autre extrémité du câble doit être connectée au boîtier noir, qui sera installé lors de la prochaine étape. Il ne s'insère que dans un seul sens, veillez donc à bien aligner le connecteur avant de le brancher.

<figure data-latex-placement="H">
<img src="figures/bb_connection.jpg" style="width:80.0%" />
<figcaption>Connexion du boîtier noir</figcaption>
</figure>

## Positionnement du boîtier noir

Après avoir décidé où placer l'écran, vous devez brancher le boîtier noir.

Le boîtier noir doit être connecté à la prise OBD2 de la voiture, qui se trouve à l'intérieur de la boîte à gants gauche de la Twizy. Si vous ne l'avez jamais ouverte auparavant, vous trouverez un petit cache en plastique à retirer pour accéder au port OBD2. Une fois l'accès dégagé, branchez simplement le boîtier noir et assurez-vous qu'il est solidement connecté. Il ne s'insère que dans un seul sens, veillez donc à bien aligner le connecteur avant de le brancher.

<figure data-latex-placement="H">
<img src="figures/obd_connector.png" style="width:80.0%" />
<figcaption>Emplacement du connecteur OBD2 dans la Twizy</figcaption>
</figure>

**Ce n'est qu'après avoir connecté l'écran** que vous pourrez activer l'interrupteur du boîtier noir. Et l'installation est terminée ! Vous pouvez maintenant démarrer votre Twizy et profiter des fonctionnalités du ToM+.

# Explication de l'interface utilisateur de base

## Liste de la signification des icônes {#sec:icon_list}

L'interface utilisateur (UI) de ToM est très intuitive et facile à utiliser, et chaque donnée est représentée par une icône spécifique qui rappelle généralement à quoi cette donnée peut être utile. Voici la liste de toutes les icônes que vous pouvez trouver sur le ToM ainsi que leur signification.

### Icônes de page {#sec:page_icon_list}

Les icônes de page sont les icônes situées sur la ligne inférieure de l'écran du ToM+. Elles sont utilisées pour basculer entre les différentes pages. Depuis la dernière mise à jour, elles ont été remises au goût du jour avec un style métallique 3D.

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/BatteryV2.png){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------- -------------------------------------------------------------
  ![image](icons/Motor.png){height="8mm"}   

  ----------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------------ -------------------------------------------------------------
  ![image](icons/BatteryInfo2.png){height="8mm"}   

  ------------------------------------------------ -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------- -------------------------------------------------------------
  ![image](icons/Alarm.PNG){height="8mm"}   

  ----------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------- -------------------------------------------------------------
  ![image](icons/Error.png){height="8mm"}   

  ----------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------- -------------------------------------------------------------
  ![image](icons/TripLog.png){height="8mm"}   

  ------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/Gyroscope.png){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------------ -------------------------------------------------------------
  ![image](icons/Street0Ok_v2.png){height="8mm"}   

  ------------------------------------------------ -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------- -------------------------------------------------------------
  ![image](icons/3Dots.PNG){height="8mm"}   

  ----------------------------------------- -------------------------------------------------------------
:::

### Groupe Batterie {#sec:item_numbers}

::: tcolorbox
  ---------------------------------------------- -------------------------------------------------------------
  ![image](icons/BatterySoc.jpg){height="8mm"}   

  ---------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------------- -------------------------------------------------------------
  ![image](icons/BatterySoh.jpg){height="8mm"}   

  ---------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------------- -------------------------------------------------------------
  ![image](icons/BatteryKwh.jpg){height="8mm"}   

  ---------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  -------------------------------------------- -------------------------------------------------------------
  ![image](icons/BatteryA.jpg){height="8mm"}   

  -------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------------ -------------------------------------------------------------
  ![image](icons/BatteryA+red.png){height="8mm"}   

  ------------------------------------------------ -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/BatteryKw.png){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/Battery3°.jpg){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/BatteryV2.jpg){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  -------------------------------------------- -------------------------------------------------------------
  ![image](icons/BatteryV.jpg){height="8mm"}   

  -------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------------- -------------------------------------------------------------
  ![image](icons/BatteryDiff.png){height="8mm"}   

  ----------------------------------------------- -------------------------------------------------------------
:::

### Groupe Recharge

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/CEta.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------- -------------------------------------------------------------
  ![image](icons/Charge°.png){height="8mm"}   

  ------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------------- -------------------------------------------------------------
  ![image](icons/ChargedKwh.png){height="8mm"}   

  ---------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/ChargeKwh.png){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

### Groupe Moteur

::: tcolorbox
  -------------------------------------------- -------------------------------------------------------------
  ![image](icons/MotoRPM2.jpg){height="8mm"}   

  -------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------- -------------------------------------------------------------
  ![image](icons/MotorNm.jpg){height="8mm"}   

  ------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------- -------------------------------------------------------------
  ![image](icons/Motor°2.jpg){height="8mm"}   

  ------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/Sev°.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

### Groupe Port d'extension

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/Pin1.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/Pin2.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

### Groupe Gyroscope

::: tcolorbox
  ------------------------------------------ -------------------------------------------------------------
  ![image](icons/InclDX.PNG){height="8mm"}   

  ------------------------------------------ -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------ -------------------------------------------------------------
  ![image](icons/InclSX.PNG){height="8mm"}   

  ------------------------------------------ -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------------- -------------------------------------------------------------
  ![image](icons/UphillTwizy.png){height="8mm"}   

  ----------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------------- -------------------------------------------------------------
  ![image](icons/DownhillTwizy.png){height="8mm"}   

  ------------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------- -------------------------------------------------------------
  ![image](icons/GyroAcc.JPG){height="8mm"}   

  ------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------- -------------------------------------------------------------
  ![image](icons/Gtemp.PNG){height="8mm"}   

  ----------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------- -------------------------------------------------------------
  ![image](icons/Timer.PNG){height="8mm"}   

  ----------------------------------------- -------------------------------------------------------------
:::

### Groupe Trajet

::: tcolorbox
  --------------------------------------- -------------------------------------------------------------
  ![image](icons/tKm.png){height="8mm"}   

  --------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/tKmh.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/tKmR.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/tkWh.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------- -------------------------------------------------------------
  ![image](icons/tkWh100.png){height="8mm"}   

  ------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  -------------------------------------------- -------------------------------------------------------------
  ![image](icons/tkWh1min.png){height="8mm"}   

  -------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------ -------------------------------------------------------------
  ![image](icons/tTimer.png){height="8mm"}   

  ------------------------------------------ -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------- -------------------------------------------------------------
  ![image](icons/tUphill.png){height="8mm"}   

  ------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/tDownhill.png){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

### Groupe Tableau de bord

::: tcolorbox
  --------------------------------------- -------------------------------------------------------------
  ![image](icons/ODO.png){height="8mm"}   

  --------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------- -------------------------------------------------------------
  ![image](icons/Kmh.png){height="8mm"}   

  --------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/KmhR.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------- -------------------------------------------------------------
  ![image](icons/KmRCalc.png){height="8mm"}   

  ------------------------------------------- -------------------------------------------------------------
:::

[]{#fig:calculated_kilometers_left label="fig:calculated_kilometers_left"}

## Page du tableau de bord

Cette section couvre l'explication de la page du tableau de bord, qui est la page principale du ToM+, et donc probablement celle que vous utiliserez le plus. Dans l'image ci-dessous, j'ai numéroté les parties les plus importantes et j'expliquerai chacune d'elles dans les paragraphes suivants.

<figure id="fig:dashboard_layout" data-latex-placement="H">
<img src="figures/dashboard_numbers.PNG" style="width:80.0%" />
<figcaption>Page du tableau de bord avec les parties numérotées.</figcaption>
</figure>

**1**

: Rapport engagé actuel du véhicule, généralement affiché également sur le tableau de bord d'origine.

**2**

: Une valeur choisie entre le couple, la consommation d'énergie et la consommation de courant, qui est utilisée pour remplir la barre de puissance décrite à l'élément 6. Appuyez sur la valeur pour faire défiler les trois options.

**3**

: Icône d'état d'erreur, affichée lorsqu'une erreur est présente.

**4**

: Affiche le trajet actif. Appuyez sur l'icône pour ouvrir la page du trajet.

**5**

: Icônes pour MQTT et Wi-Fi. Grisées en cas de déconnexion, et colorées une fois connecté. Appuyez sur les icônes si vous souhaitez effectuer une nouvelle recherche Wi-Fi ou une reconnexion MQTT.

**6**

: Barre de puissance affichant la valeur sélectionnée à l'élément 2. En partant de la ligne centrale, la barre se remplit de gauche à droite lors de l'accélération, et de droite à gauche lors du freinage régénératif. La barre se remplit avec un dégradé de couleur dans chaque direction, et les **valeurs maximales et minimales sont personnalisables** sur la page BigToM du serveur web.

**7**

: Affiche la vitesse instantanée du véhicule. Vous pouvez choisir entre km/h et mph dans la page Informations avancées et paramètres du serveur web.

**8**

: Icône moteur, appuyez dessus pour ouvrir la page moteur.

**9**

: Icône colorée avec dégradé de la batterie, appuyez dessus pour ouvrir la page d'informations de la batterie.

**10**

: Valeurs affichées supplémentaires, vous pouvez naviguer entre elles en appuyant sur l'icône pour les modifier.

**11**

: Affiche l'heure et la date, basculez entre elles en appuyant dessus.

**12**

: Limite d'alerte de vitesse personnalisable (verte, jaune ou rouge), voir la Section [4.4.14](#sec:web_btom_tom_sets){reference-type="ref" reference="sec:web_btom_tom_sets"} pour l'activer.

## La disposition des pages {#sec:main-layout}

La disposition peut être divisée en deux parties principales, que nous verrons en détail dans les deux paragraphes suivants. La première est le moniteur de données qui dispose de fonctionnalités pour modifier les données affichées au premier plan en les choisissant parmi celles répertoriées dans la barre latérale. La seconde est la barre d'icônes d'état, généralement située au bas de la page. Les pages batterie, moteur, gyroscope et trajet partagent la même disposition, comme illustré sur l'image.

<figure data-latex-placement="H">
<img src="figures/engine_page.jpg" style="width:80.0%" />
<figcaption>Exemple de la disposition partagée (la page moteur).</figcaption>
</figure>

Sur le côté gauche de l'écran, comme vous pouvez le voir sur la photo, se trouve une liste de quatre valeurs, regroupées dans une grille minimale. Chaque valeur est associée à son unité de mesure et à une petite icône, unique pour chaque donnée et toutes répertoriées dans la Section [3.1](#sec:icon_list){reference-type="ref" reference="sec:icon_list"}. Au-dessus de la valeur se trouve une barre de progression orange qui représente à quel point la valeur est grande (ou petite) par rapport à sa valeur maximale (ou minimale).\
La zone droite de l'écran est principalement occupée par la donnée au premier plan (ou simplement la donnée sélectionnée). Elle comporte une grande icône Twizy entourée d'une barre de progression en forme d'arc qui remplit la même fonction que la plus petite abordée précédemment, à la seule différence qu'elle compte 32 étapes au lieu de 16 seulement. Aux extrémités de la barre de progression se trouve la plage ou le multiplicateur de la valeur affichée au centre de la page, qui est celle associée à l'icône affichée juste au-dessus.\
En bas, se trouve une liste d'icônes utilisées pour basculer entre les différentes pages du ToM+. Les icônes sont les mêmes pour toutes les pages, et elles sont toutes répertoriées dans la Section [3.1.1](#sec:page_icon_list){reference-type="ref" reference="sec:page_icon_list"}. Dans le coin supérieur gauche, une petite icône indique le rapport engagé actuel du véhicule. Si vous appuyez dessus, **elle vous ramènera à la page du tableau de bord** que nous venons d'évoquer. Dans le coin supérieur droit, trois petits points permettent d'ouvrir la page des paramètres lorsqu'on appuie dessus. Enfin, sur la longue ligne blanche en bas de l'écran, se trouve la barre d'état avec quelques icônes que nous aborderons plus tard.

### Changer la donnée au premier plan

Modifier la donnée affichée au premier plan est très simple et intuitif. Il vous suffit d'appuyer sur l'icône de la donnée que vous souhaitez afficher au premier plan et les valeurs s'échangeront. De cette façon, vous pouvez également réorganiser les données sur le côté gauche de l'écran, ce qui est très pratique si vous souhaitez avoir une donnée spécifique dans un ordre arbitraire.

<figure data-latex-placement="H">
<img src="figures/change_foreground.jpg" style="width:70.0%" />
<figcaption>Exemple de changement de la donnée au premier plan (sur la page moteur).</figcaption>
</figure>

À titre d'exemple, sur l'image ci-dessus, l'utilisateur a appuyé sur l'icône du régime moteur, qui est actuellement affiché sur le côté gauche de l'écran. Les deux valeurs se sont permutées et le régime moteur est désormais affiché au premier plan, tandis que le SOC de la batterie est affiché dans la grille de gauche.

### Changer de page active

Pour changer la page active, vous pouvez appuyer sur l'icône de la page vers laquelle vous souhaitez basculer, située sur la ligne inférieure de l'écran. L'icône deviendra orange et la nouvelle page s'affichera. Dans l'image, la page active est la page moteur.

<figure data-latex-placement="H">
<img src="figures/changing_page.jpg" style="width:70.0%" />
<figcaption>Exemple de changement de page active (sur la page moteur).</figcaption>
</figure>

Chacune de ces actions peut être effectuée à l'aide du bouton situé sur le commodo d'essuie-glace droit, ce qui est très pratique en conduisant, car vous pouvez garder les yeux sur la route et les mains sur le volant. Le bouton peut être utilisé pour faire défiler les différentes pages, pour modifier la donnée au premier plan et plus encore. Il sera décrit en détail dans la Section [4.4.7.5](#sec:web_wiper_stalk){reference-type="ref" reference="sec:web_wiper_stalk"}.

### La barre d'icônes d'état {#sec:status_icon_bar}

Sous les boutons de changement de page abordés au paragraphe précédent, se trouve une longue ligne blanche qui vous indique l'état de la connexion réseau ainsi que le déclenchement des alarmes ou des erreurs. Au début de la ligne, comme vous pouvez le voir sur l'image, se trouve une petite icône twizy avec un numéro : c'est un bouton qui vous mènera à la page du trajet, qui sera abordée plus tard dans la Section [3.6](#sec:trip_page){reference-type="ref" reference="sec:trip_page"}. Voyons maintenant la barre d'icônes d'état.

<figure data-latex-placement="H">
<img src="figures/status_icon_bar.jpg" style="width:70.0%" />
<figcaption>La barre d’icônes d’état.</figcaption>
</figure>

En partant du côté droit de l'image, vous verrez un symbole d'onde bleu magnétique qui représente l'état de la connexion **Wi-Fi**. En effet, s'il est allumé et fixe comme ci-dessus, cela signifie que ToM est connecté à un réseau Wi-Fi, qu'il s'agisse d'un réseau public ou d'un réseau de la liste que vous avez définie. Lorsque l'icône est grisée, ToM n'est connecté à aucun réseau et recherchera à nouveau des réseaux Wi-Fi après une période de recharge de cinq minutes. Vous pouvez également forcer un nouveau balayage dès que possible en appuyant sur l'icône. Enfin, si l'icône clignote, ToM a effectué une recherche Wi-Fi, a trouvé un ou plusieurs réseaux et tente de se connecter à l'un d'eux.\
L'icône suivante est un nuage violet contenant le texte **« MQTT »** et, comme vous pouvez le deviner, elle représente l'état de la connexion **MQTT**. La position de cette icône est fixe et ne peut pas être modifiée, tout comme celle du Wi-Fi. Une autre similitude avec l'icône précédente est qu'elle peut être soit fixe, soit grisée avec le même code couleur que précédemment.\
Ensuite, nous avons l'icône d'erreur, qui est un rectangle rouge contenant le texte **« ERR »**. Elle s'affichera lorsqu'une erreur est présente ou sera masquée lorsqu'il n'y a pas d'erreur.\
Enfin, nous avons les icônes d'alarme, représentées par des étoiles colorées. Les étoiles disponibles sont celles présentées sur l'image ; vous pouvez sélectionner celle à utiliser pour chaque alarme sur la page Déclencheurs d'alarme du serveur web. Vous pouvez y choisir de les faire clignoter ou non.

<figure id="fig:alarm_icons" data-latex-placement="H">
<img src="figures/alarm_icons.png" style="width:70.0%" />
<figcaption>Les icônes d’alarme.</figcaption>
</figure>

### Fenêtres surgissantes (Pop-ups)

Sur ces pages, des fenêtres surgissantes apparaîtront en fonction de vos configurations définies sur la page « Déclencheurs d'alarme » du serveur web. Il existe deux types principaux de pop-ups : le premier ne disparaîtra pas tant que vous ne l'aurez pas remarqué et appuyé dessus (ce type bloquera l'ensemble du système, mettant en pause les valeurs de la grille de gauche ainsi que la valeur au premier plan). Sinon, si vous ne souhaitez pas être dérangé en conduisant, vous pouvez utiliser le second type de pop-up, spécialement conçu pour disparaître automatiquement après 10 secondes.\
Vous pouvez voir ici un exemple du type de pop-up le plus simple où l'icône d'avertissement entourée continuera de clignoter. Comme vous pouvez le constater, elle est composée d'un encadré jaune avec un contour pointillé qui contient l'icône de la valeur et la valeur elle-même qui a déclenché l'alarme préalablement définie sur la page du serveur web (température du moteur = 35° C).

<figure data-latex-placement="H">
<img src="figures/pop-up.PNG" style="width:70.0%" />
<figcaption>Un exemple de fenêtre surgissante (pop-up).</figcaption>
</figure>

## La page d'informations sur la batterie

La page d'informations sur la batterie vous fournira des informations plus détaillées sur chaque cellule de la batterie. Comme vous le savez peut-être, les batteries standards de la Twizy possèdent 14 cellules et un capteur de température partagé pour chaque paire de cellules. Sur cette page, vous pouvez surveiller la tension de chaque cellule ainsi que sa température, et avoir une vue d'ensemble de la tension totale de la batterie. L'image montre son apparence habituelle.

<figure data-latex-placement="H">
<img src="figures/binfo_page.jpg" style="width:80.0%" />
<figcaption>La page d’informations sur la batterie.</figcaption>
</figure>

### Vérification de la tension et de la température

Comme indiqué sur l'image ci-dessus, sur le côté gauche de la page se trouve une ligne blanche en forme de batterie qui contient un petit tableau avec les tensions des sept premières cellules. Pour voir les tensions des cellules restantes, appuyez sur le symbole de flèche orange et blanche (celui entouré sur la photo suivante) et la grille affichera les valeurs suivantes.

Si vous appuyez à nouveau sur ce même bouton fléché, les données affichées changeront à nouveau pour devenir les températures des cellules, exprimées en degrés Celsius. La valeur au premier plan changera également, et comme vous pouvez le remarquer d'après l'icône située au-dessus, elle affiche la température totale de la batterie, qui est identique à celle de chaque cellule dans cet exemple. Reportez-vous à l'image ci-dessous pour voir la modification.

<figure data-latex-placement="ht">
<figure>
<img src="figures/binfo_page2.jpg" />
<figcaption>Tensions des cellules restantes.</figcaption>
</figure>
<figure>
<img src="figures/binfo_page3.jpg" />
<figcaption>Températures des cellules.</figcaption>
</figure>
<figcaption>Températures des cellules.</figcaption>
</figure>

### La page d'informations condensées de la batterie {#sec:condensed_binfo}

En appuyant à nouveau sur le même bouton, vous accéderez à une page spéciale qui contient toutes les données abordées dans le paragraphe précédent en une seule fois.

<figure data-latex-placement="H">
<img src="figures/binfo_page_condensed.png" style="width:80.0%" />
<figcaption>La page d’informations condensées de la batterie.</figcaption>
</figure>

Sur la photo ci-dessus, vous verrez que l'écran est divisé en deux parties. La première est la même ligne blanche en forme de batterie, mais un peu plus grande, afin de contenir toutes les valeurs de tension et de température. La température est située entre les deux cellules qui partagent ce capteur de température. Sur le côté droit de la page, vous pouvez voir la valeur qui était auparavant affichée au premier plan, c'est-à-dire la tension totale de la batterie et la température totale de la batterie. Il y a également la valeur du SOC en première position car elle est toujours utile.\
Sur cette page, il n'y avait pas assez d'espace pour placer les boutons de changement de page, car il est plus important d'avoir les icônes d'état dont nous avons parlé précédemment. Si vous devez changer de page, vous pouvez appuyer sur le bouton de sortie dans le coin inférieur droit, puis vous serez redirigé vers une page contenant les commandes permettant de modifier la page active.\
Une note importante de la dernière mise à jour concerne la différence entre la cellule ayant la tension minimale et celle ayant la tension maximale, respectivement représentées par un point bleu et un point rouge. Cette valeur est très importante car elle peut vous indiquer si la batterie est en bonne santé ou non. Si la différence est trop élevée, cela signifie que la batterie est déséquilibrée et cela pourrait être le signe d'un problème. ToM+ vous affichera cette valeur dans la page d'informations condensées de la batterie, et vous pouvez également définir un déclencheur d'alarme sur le serveur web pour être averti lorsque la différence est trop élevée.\
Vous pouvez décider dans les paramètres si cette page condensée de la batterie est affichée comme page par défaut lorsque vous appuyez sur le bouton d'informations de la batterie ou non. Le processus est illustré dans la Section [3.10](#sec:settings_page){reference-type="ref" reference="sec:settings_page"}. Si vous sélectionnez l'option permettant d'avoir les quatre pages vues dans ce paragraphe, vous pouvez également appuyer sur le bouton fléché sur la page condensée pour revenir aux autres pages d'informations de la batterie.

## La page du journal des alarmes {#sec:alarm_log}

Sur cette page, vous pourrez consulter tous les déclenchements d'alarmes, au cas où vous en auriez manqué un ou si vous les avez mis en sourdine pour ne pas être dérangé en conduisant. Voyons à quoi elle ressemble.

<figure data-latex-placement="H">
<img src="figures/alarm_page.jpg" style="width:80.0%" />
<figcaption>La page du journal des alarmes en 3D.</figcaption>
</figure>

L'image montre un petit tableau qui contient l'élément ayant provoqué le déclenchement de l'alarme, associé à son icône et à sa valeur. J'ai ensuite ajouté la date et l'heure (disponibles si connecté à un réseau la première fois) pour savoir quand cet enregistrement a été ajouté à la liste.\
Dans les images suivantes (avec l'ancien design), la plupart des enregistrements sont liés au SOC de la batterie, spécifiquement lorsqu'il descend en dessous de 30%. Vous découvrirez comment définir vos propres alarmes sur le serveur web dans la Section [4.4.8](#sec:web_alarm_triggers){reference-type="ref" reference="sec:web_alarm_triggers"}.

<figure data-latex-placement="H">
<img src="figures/alarm_log_old1.png" style="width:70.0%" />
<figcaption>La page du journal des alarmes en 3D.</figcaption>
</figure>

### Vérification des déclenchements d'alarmes plus anciens

Si vous avez besoin de voir des déclenchements d'alarmes plus anciens qui n'apparaissent pas dans la liste des sept premiers, vous pouvez appuyer sur l'icône d'avertissement jaune en haut du tableau, ce qui remplacera les valeurs affichées par les plus anciennes. Vous pouvez effectuer cette action deux fois, car ToM est capable de stocker jusqu'à 21 déclenchements d'alarmes et oublie les plus anciens.

<figure data-latex-placement="H">
<img src="figures/alarm_log_old2.png" style="width:100.0%" />
<figcaption>Changement des déclenchements affichés.</figcaption>
</figure>

Comme vous pouvez le voir sur ces deux photos de la page du journal des alarmes, lorsque j'ai appuyé sur le bouton d'avertissement jaune entouré, les données affichées ont changé pour laisser place à des données plus anciennes, comme vous pouvez le constater en comparant les dates. Le compteur d'éléments sur la gauche a également changé (8--14).

### Suppression d'un déclencheur d'alarme {#sec:delete_log_record}

Si vous n'avez plus besoin d'un ou plusieurs enregistrements, vous pouvez choisir d'en supprimer certains. Sélectionnez un ou plusieurs enregistrements à supprimer définitivement en appuyant sur leur date ou leur heure (une petite coche rouge apparaîtra à côté des enregistrements choisis). Appuyez ensuite sur l'icône de corbeille entourée de jaune sur la deuxième photo pour supprimer les enregistrements sélectionnés. Ces enregistrements disparaîtront et seront remplacés par les enregistrements suivants, provoquant un décalage de l'ensemble de la liste comme vous pouvez le remarquer sur la deuxième image.

<figure data-latex-placement="H">
<img src="figures/alarm_log_old3.jpg" style="width:100.0%" />
<figcaption>Suppression des déclenchements d’alarmes sélectionnés.</figcaption>
</figure>

Sur cette page, il n'y a pas de barre d'icônes d'état ni de boutons pour changer de page, puisqu'il s'agit d'une page de configuration qui n'a pas besoin de telles commandes. Pour quitter, appuyez sur le bouton fléché dans le coin inférieur droit et ToM vous ramènera à la page où vous étiez avant de consulter la page du journal des alarmes, à partir de laquelle vous pourrez à nouveau modifier la page active.

## La page du trajet {#sec:trip_page}

Cette page est capable de stocker les données d'un trajet *(un trajet correspond au temps écoulé entre le moment où vous commencez à conduire et celui où vous éteignez votre Twizy)* puis de décider de conserver ou de rejeter ces valeurs lorsque vous recommencez à conduire. Vous pouvez enregistrer simultanément jusqu'à cinq données de trajet. La disposition est la même que celle de la page principale, les commandes permettant de modifier l'ordre des valeurs ou les données au premier plan ont donc déjà été abordées dans la Section [3.3](#sec:main-layout){reference-type="ref" reference="sec:main-layout"}. Les paragraphes suivants expliquent comment réinitialiser un trajet et comment changer le trajet en cours.

<figure data-latex-placement="H">
<img src="figures/trip_page_full.jpg" style="width:80.0%" />
<figcaption>La page du trajet.</figcaption>
</figure>

### Changer le trajet en cours

Si vous souhaitez commencer à enregistrer les données sur un trajet spécifique choisi de 1 à 5, vous pouvez appuyer sur l'icône de trajet entourée de jaune dans l'image précédente. Lorsque vous appuyez dessus pour la première fois, vous serez dirigé vers le trajet n° 1 et des appuis successifs feront défiler tous les trajets disponibles, afin que vous puissiez sélectionner celui que vous souhaitez démarrer ou poursuivre.\
Pour voir sur quel trajet ToM enregistre actuellement, reportez-vous au chiffre orange sur l'icône de trajet. Une fois le trajet désiré choisi, vous pouvez également changer la page active si vous le souhaitez, sans perdre le trajet sélectionné, car ToM continuera d'enregistrer les valeurs même si la page du trajet n'est pas affichée à l'écran.

### Désactiver l'enregistrement du trajet

Dans cet exemple, je suis actuellement sur la page moteur et j'enregistre les données sur la cinquième page de trajet, comme l'indique le petit chiffre orange près de l'icône du trajet. Si vous souhaitez mettre en pause l'enregistrement du trajet, vous pouvez le faire sur ToM+ en **maintenant enfoncé pendant trois secondes le bouton de trajet** pendant qu'une autre page est active (dans cet exemple, celle de la batterie).\

<figure data-latex-placement="ht">
<figure>
<img src="figures/trip_page_on.jpg" />
<figcaption>Enregistrement de trajet actif sur le trajet 5.</figcaption>
</figure>
<figure>
<img src="figures/trip_page_off.jpg" />
<figcaption>Enregistrement de trajet en pause.</figcaption>
</figure>
<figcaption>Enregistrement de trajet en pause.</figcaption>
</figure>

Une fois relâché, ToM+ modifie la petite icône de trajet pour afficher le symbole de carte au lieu du numéro de trajet, afin de vous informer qu'il n'enregistre plus les données (deuxième image). Lorsque vous êtes prêt à reprendre l'enregistrement du trajet, appuyez sur la page du trajet jusqu'à trouver le trajet souhaité en faisant défiler tous ceux disponibles.

### Réinitialiser un trajet

Si vous souhaitez effacer les données d'un trajet spécifique, vous pouvez le sélectionner et **maintenir enfoncé le bouton du trajet pendant trois secondes**. Une fois relâché, vous devriez remarquer que toutes les valeurs du trajet sur la page ont été réinitialisées (généralement à zéro). La différence entre cette action et la précédente est que dans ce cas, les données du trajet sont effacées, tandis que dans la précédente, les données du trajet sont simplement mises en pause. De plus, vous devez ici être sur la page du trajet, alors que pour la précédente, vous devez être sur n'importe quelle autre page.

## La page de l'historique des trajets {#sec:trip_history}

Cette page stocke les données des vingt derniers trajets et sa disposition est la même que celle du journal des alarmes. Les valeurs sont mises à jour et enregistrées uniquement lorsque le trajet sélectionné est le **numéro 5**.

### Comment accéder à la page de l'historique des trajets

Cette page n'est pas accessible depuis la page principale, mais vous pouvez y accéder en **appuyant longuement sur l'icône du journal des alarmes** sur la ligne inférieure de l'écran jusqu'à ce qu'elle change. En effet, la page d'historique des trajets n'est pas une page que vous utiliserez souvent, il a donc été décidé de la masquer de la page principale pour gagner de l'espace, tout comme la page d'erreur. Ainsi, la séquence de pages disponibles en **appuyant longuement sur l'icône du journal des alarmes** est : page du journal des alarmes (Section [3.5](#sec:alarm_log){reference-type="ref" reference="sec:alarm_log"}) $\rightarrow$ page d'erreur (Section [3.8](#sec:error_page){reference-type="ref" reference="sec:error_page"}) $\rightarrow$ page de l'historique des trajets $\rightarrow$ retour à la page du journal des alarmes, chacune avec son icône respective.\

<figure data-latex-placement="H">
<img src="figures/enter_trip_log_page.jpg" style="width:80.0%" />
<figcaption>L’icône pour accéder à la page de l’historique des trajets.</figcaption>
</figure>

### Commandes principales de la page d'historique des trajets

<figure data-latex-placement="H">
<img src="figures/trip_history_page.jpg" style="width:80.0%" />
<figcaption>La page de l’historique des trajets.</figcaption>
</figure>

Sur cette image, vous pouvez voir les sept premiers trajets enregistrés dans la liste, avec leur date et heure, ainsi que la distance parcourue. Vous pouvez facilement modifier la donnée affichée sur chaque ligne en appuyant sur l'icône de la donnée comme indiqué ci-dessous. Les données défileront parmi la plupart des données de trajet disponibles, vous permettant de choisir celle à afficher. Dans les images suivantes, vous pouvez voir la même page avec la consommation d'énergie du trajet et la vitesse moyenne.

<figure data-latex-placement="ht">
<figure>
<img src="figures/trip_log_kwh.jpg" />
<figcaption>Affichage de la consommation d’énergie du trajet.</figcaption>
</figure>
<figure>
<img src="figures/trip_log_kmh.jpg" />
<figcaption>Affichage de la vitesse moyenne du trajet.</figcaption>
</figure>
<figcaption>Affichage de la vitesse moyenne du trajet.</figcaption>
</figure>

Sur le serveur web, vous pouvez les consulter toutes en même temps ; cela sera abordé dans la Section [4.4.5](#sec:web_trip_history){reference-type="ref" reference="sec:web_trip_history"}.

## La page d'erreur {#sec:error_page}

Cette page est similaire à la page du journal des alarmes et à la page d'historique des trajets, mais elle vous affichera les dernières erreurs DTC survenues. Les commandes permettant de supprimer des enregistrements ou de consulter les plus anciens ont déjà été abordées dans la Section [3.5](#sec:alarm_log){reference-type="ref" reference="sec:alarm_log"}.

### Comment accéder à la page d'erreur

Cette page n'est pas accessible depuis la page principale, mais vous pouvez y accéder en **appuyant longuement sur l'icône du journal des alarmes** dans la ligne inférieure de l'écran jusqu'à ce qu'elle change. Comme nous l'avons vu précédemment, la séquence des pages disponibles par appui long sur l'icône du journal des alarmes est la suivante : page du journal des alarmes (Section [3.5](#sec:alarm_log){reference-type="ref" reference="sec:alarm_log"}) $\rightarrow$ page d'erreur $\rightarrow$ page de l'historique des trajets (Section [3.7](#sec:trip_history){reference-type="ref" reference="sec:trip_history"}) $\rightarrow$ retour à la page du journal des alarmes, chacune avec son icône respective.\

<figure data-latex-placement="ht">
<figure>
<img src="figures/enter_error_page.jpg" />
<figcaption>L’icône pour accéder à la page d’erreur.</figcaption>
</figure>
<figure>
<img src="figures/error_page.jpg" />
<figcaption>Affichage de la page d’erreur.</figcaption>
</figure>
<figcaption>Affichage de la page d’erreur.</figcaption>
</figure>

### Commandes principales de la page d'erreur

Comme vous pouvez le voir sur la deuxième image ci-dessus, la page d'erreur est similaire à la page du journal des alarmes. Elle affiche une liste des 14 dernières erreurs survenues, avec leur ODO, le numéro DTC, le numéro DF s'il est disponible, et une icône représentative. Reportez-vous à la page correspondante sur le serveur web pour plus d'informations telles que le SOC, la vitesse et une brève description (Section [4.4.15](#sec:web_diagnostic){reference-type="ref" reference="sec:web_diagnostic"}).\
En appuyant sur l'icône de l'erreur (entourée en jaune sur l'image), vous pouvez faire défiler les pages des erreurs enregistrées, qui sont au nombre de 14 au total. La première page affiche les 7 dernières erreurs, tandis que la seconde affiche les plus anciennes. Pour **supprimer les enregistrements d'erreurs** à la fois sur cette page et sur la voiture, cliquez simplement sur l'icône de corbeille.\
Comme sur d'autres pages, l'espace n'était pas suffisant pour placer les boutons de changement de page, vous pouvez donc appuyer sur le bouton de sortie dans le coin inférieur droit pour revenir à la page précédente, puis modifier la page active si vous le souhaitez.

## La page de recharge {#sec:charging_page}

Cette page ne s'affiche pas en conduisant et il n'y a pas de bouton spécifique pour la visualiser. Cela est principalement dû au fait que cet écran de recharge apparaît automatiquement lorsque la Twizy est actuellement en cours de charge.

Comme vous pouvez le voir sur l'image, la disposition est la même que celle de la page du tableau de bord. Le SOC actuel est affiché au centre, remplaçant la valeur de la vitesse.\
Une animation démarrera également, avec une vitesse différente selon le niveau de puissance de charge. Sur la photo ci-dessous se trouvent également des données spécifiques à la recharge, que vous pouvez modifier dans les paramètres comme expliqué ultérieurement. Sur cette page, vous n'avez pas la barre d'icônes d'état, mais vous disposez toujours des icônes d'état du réseau dans le coin inférieur droit, puisque vous pouvez également surveiller les valeurs de recharge de votre voiture lorsqu'elle est éteinte. En effet, ToM+ s'allumera automatiquement lorsque vous brancherez votre Twizy sur une source d'alimentation valide.

<figure data-latex-placement="H">
<img src="figures/charging_page.jpg" style="width:80.0%" />
<figcaption>La page de recharge.</figcaption>
</figure>

**1**

: Puissance actuelle stockée dans la batterie, exprimée en $kWh$.

**2**

: Une valeur choisie entre le couple, la consommation d'énergie et la consommation de courant, qui est utilisée pour remplir la partie bleue de la barre de puissance. Appuyez sur la valeur pour faire défiler les trois options.

**3**

: Puissance de charge actuelle, exprimée en $kW$, utilisée pour remplir le côté droit de la barre de puissance.

**4**

: Affiche l'ETA, c'est-à-dire le temps estimé pour terminer la charge.

**5**

: Le SOC actuel, c'est-à-dire l'état de charge de la batterie, exprimé en %.

**6**

: Valeurs affichées supplémentaires, vous pouvez naviguer entre elles en appuyant sur l'icône pour modifier.

**7**

: Icônes pour MQTT et Wi-Fi. Grisées en cas de déconnexion, et colorées une fois connecté. Appuyez sur les icônes si vous souhaitez effectuer une nouvelle recherche Wi-Fi ou une reconnexion MQTT.

**8**

: Bouton de raccourci pour ouvrir la page des paramètres, afin d'accéder à des réglages plus avancés.

## La page des paramètres {#sec:settings_page}

Afin de rendre ToM beaucoup plus personnalisable, voici la page des paramètres, accessible en appuyant sur les trois points dans le coin supérieur droit sur n'importe quelle page principale. Vous pouvez désormais facilement modifier l'apparence de base de votre ToM personnel.

<figure id="fig:settings_page" data-latex-placement="H">
<img src="figures/settings_page1.jpg" style="width:80.0%" />
<figcaption>La première page des paramètres.</figcaption>
</figure>

La dernière ligne vous donnera des informations sur votre ToM personnel et affichera :

- Le **numéro de série** de votre ToM dans le premier champ (censuré sur la figure ci-dessus)

- La version du microprogramme (firmware) du boîtier noir (ESP) (actuellement 2.4 sur la figure)

- La version du microprogramme (firmware) de l'écran tactile LCD (actuellement 2.4 sur la figure)

Vous pouvez effectuer la mise à jour vers la dernière version du microprogramme comme expliqué dans la Section [5](#sec:update_procedure){reference-type="ref" reference="sec:update_procedure"}.

### Première page des paramètres

Comme vous pouvez le remarquer sur l'image ci-dessus, le bouton entouré dans le coin supérieur droit vous indiquera sur quelle page de paramètres vous vous trouvez actuellement. Dans ce cas, il s'agit de la première, mais vous pouvez appuyer dessus pour passer à la seconde. La première page concerne principalement l'apparence du ToM+, tandis que la seconde concerne le comportement du ToM+ et d'autres paramètres avancés.

#### Personnalisation des valeurs de page

Si vous souhaitez modifier l'ordre des données affichées dans l'une des pages ou même combiner des données provenant de différentes pages, vous pouvez le faire dans la page des paramètres, en suivant ces étapes.

<figure data-latex-placement="H">
<img src="figures/settings_page1_values.jpg" style="width:80.0%" />
<figcaption>Personnalisation des valeurs de page.</figcaption>
</figure>

En appuyant sur la première icône, vous ferez défiler toutes les pages disponibles dont les icônes ont été expliquées précédemment dans la Section [3.1.1](#sec:page_icon_list){reference-type="ref" reference="sec:page_icon_list"} et qui vous permettront de personnaliser les valeurs pour cette page spécifique. Dans l'image ci-dessus, l'utilisateur a sélectionné la page gyroscope, donc les valeurs affichées à droite sont celles actuellement définies pour cette page.\
Chacune des cinq icônes sous l'en-tête **Displayed Data** (Données affichées) peut être personnalisée simplement en appuyant dessus, en faisant défiler toutes les données jusqu'à trouver celle souhaitée (signification des icônes expliquée dans la Section [3.1](#sec:icon_list){reference-type="ref" reference="sec:icon_list"}). Par exemple, vous pouvez également choisir de placer des données moteur sur la page batterie, combinant ainsi les deux.\

<figure id="fig:icon_arrangement" data-latex-placement="H">
<img src="figures/settings_page1_matching.jpg" style="width:80.0%" />
<figcaption>Valeurs de disposition résultantes.</figcaption>
</figure>

Après avoir personnalisé les valeurs affichées, **n'oubliez pas de sauvegarder en appuyant sur le bouton de sortie**. La nouvelle configuration apparaîtra comme indiqué sur la figure : la première donnée sera celle affichée au premier plan au centre de la page, tandis que toutes les autres seront répertoriées dans le tableau du côté gauche dans l'ordre que vous avez spécifié dans la page des paramètres.

#### Choix de la page de démarrage

Vous pouvez choisir quelle page sera la première à s'afficher lorsque vous quittez la page du tableau de bord. Pour ce faire, appuyez sur l'icône pour faire défiler toutes les pages disponibles jusqu'à trouver celle que vous souhaitez.

Dans l'image ci-dessous, l'utilisateur a sélectionné la page batterie, donc en quittant la page du tableau de bord, ToM+ l'affichera en premier.\

<figure data-latex-placement="H">
<img src="figures/settings_page1_bright.jpg" style="width:80.0%" />
<figcaption>Personnalisation de la page de démarrage et de la luminosité.</figcaption>
</figure>

#### Réglage de la luminosité de l'écran

Comme vous pouvez le voir sur l'image ci-dessus, vous pouvez régler la luminosité de l'écran en appuyant sur les boutons `-` ou `+`. La luminosité peut être réglée de 0 à 100% et la modification sera appliquée immédiatement.\

#### Activer/Désactiver la page de recharge

ToM+ dispose d'une page spécifique pour afficher des données de charge plus détaillées (Section [3.9](#sec:charging_page){reference-type="ref" reference="sec:charging_page"}). Vous pouvez choisir de la maintenir activée (*croyez-moi, cela en vaut la peine !*) ou désactivée.

Appuyez ou faites glisser le bouton vers la gauche pour choisir entre ON et OFF. Lorsque le bouton glissant est réglé sur ON, le ToM démarre et charge la page de recharge lorsque votre Twizy est en charge ; sinon, à l'état OFF, il reste éteint pendant la charge. Pour enregistrer vos modifications, appuyez sur le bouton de sortie dans le coin inférieur droit.\

<figure data-latex-placement="H">
<img src="figures/settings_page1_charge.jpg" style="width:80.0%" />
<figcaption>Personnalisation de la page de recharge et des kWh de la batterie.</figcaption>
</figure>

#### Réglage de la capacité de votre batterie

Vous pouvez définir la capacité de votre batterie en kWh, ce qui est utile si vous possédez une Twizy avec une batterie différente de celle d'origine. Cela aidera ToM+ à calculer l'autonomie restante de manière plus précise. Vous pouvez ajuster la valeur par pas de 0,1 kWh en appuyant sur les boutons `-` ou `+`, et le changement sera immédiatement appliqué. Veillez à **sauvegarder votre nouvelle configuration** en appuyant sur le bouton de sortie dans le coin inférieur droit.

#### Calibrage du module gyroscope

Si vous constatez que les données d'inclinaison du gyroscope pourraient être erronées, essayez d'appuyer sur le bouton « CALIBRATE » qui effectuera un calibrage du gyroscope. Assurez-vous d'être **sur une surface plane** avec votre Twizy avant d'effectuer cette opération, sinon vos données d'inclinaison risquent d'être encore pires. Le processus est illustré ci-dessous :

<figure data-latex-placement="H">
<img src="figures/settings_page1_calibrate.jpg" style="width:80.0%" />
<figcaption>Réglage du calibrage du gyroscope.</figcaption>
</figure>

#### Changement du mode de la page batterie

Vous pouvez choisir d'avoir uniquement la page d'informations condensées de la batterie (Section [3.4.2](#sec:condensed_binfo){reference-type="ref" reference="sec:condensed_binfo"}) lorsque vous appuyez sur le bouton d'informations de la batterie ou non.

Les deux options disponibles sont *'Condensed'* (Condensé) et *'Multiple'* (Multiple) et vous pouvez basculer entre elles en appuyant sur le texte. La modification s'appliquera dès que vous appuyez sur le bouton de sortie dans le coin inférieur droit. Le mode **Multiple** affichera les quatre pages de batterie dont nous avons parlé dans la Section [3.4.2](#sec:condensed_binfo){reference-type="ref" reference="sec:condensed_binfo"}, tandis que le mode **Condensed** n'affichera que la page condensée.\

### Seconde page des paramètres

Cette seconde page de paramètres concerne certains réglages avancés sur le processus de recharge. Pour y accéder, appuyez sur le bouton entouré dans le coin supérieur droit de la première page de paramètres et appuyez à nouveau dessus pour revenir à la première page.\

<figure data-latex-placement="H">
<img src="figures/settings_page2.jpg" style="width:80.0%" />
<figcaption>Seconde page des paramètres.</figcaption>
</figure>

#### Changement du niveau de charge

Vous pouvez choisir le niveau de charge maximal de la batterie de votre Twizy, ce qui est utile si vous souhaitez limiter la puissance absorbée par la batterie pour augmenter sa durée de vie ou pour d'autres raisons. Le niveau *'0'* signifie que le limiteur est désactivé, tandis que les niveaux *'1'* à *'7'* signifient l'utilisation du niveau de charge correspondant jusqu'au maximum disponible.

Pour augmenter ou diminuer le niveau, appuyez sur les boutons `-` ou `+`. La modification sera appliquée à la charge en cours si elle est déjà en cours, ou à la prochaine charge dans le cas contraire.\

<figure data-latex-placement="H">
<img src="figures/settings_page2_lvl.jpg" style="width:60.0%" />
<figcaption>Changement du niveau de charge.</figcaption>
</figure>

#### Contrôle manuel de la broche PIN1 d'extension

Certains utilisateurs ont signalé qu'il serait utile d'avoir un contrôle manuel de la broche PIN1 d'extension, normalement utilisée pour contrôler un chargeur auxiliaire. Ainsi, en cas de besoin, vous pouvez contrôler manuellement la broche PIN1 d'extension en appuyant sur le bouton ON/OFF. La modification sera appliquée dès que vous appuyez sur le bouton de sortie dans le coin inférieur droit.\

<figure data-latex-placement="H">
<img src="figures/settings_page2_stop.jpg" style="width:80.0%" />
<figcaption>Contrôle manuel de la broche PIN1 d’extension et arrêt du niveau de charge.</figcaption>
</figure>

#### Arrêt de la charge à un SOC spécifique

Vous pouvez choisir d'arrêter la charge à un SOC spécifique, ce qui est utile si vous souhaitez augmenter la durée de vie de la batterie. Vous pouvez régler la valeur de 0 à 100% en appuyant sur les boutons `-` ou `+`. La modification s'appliquera à la charge en cours si elle est déjà démarrée ou à la charge suivante dans le cas contraire.\

#### Effectuer une charge avec paramètres maximaux

Vous pouvez choisir d'effectuer une charge sans limites de puissance et de SOC, ce qui est utile si vous souhaitez équilibrer les cellules de la batterie de temps en temps. Vous pouvez appuyer sur le bouton pour lancer la charge avec les paramètres maximaux, qui sera appliquée à la charge en cours ou à la charge suivante.\

<figure data-latex-placement="H">
<img src="figures/settings_page2_max.jpg" style="width:80.0%" />
<figcaption>Charge avec paramètres maximaux et interruption du processus de charge.</figcaption>
</figure>

#### Interrompre le processus de charge

Vous pouvez choisir d'interrompre le processus de recharge, ce qui est utile si vous souhaitez arrêter la charge immédiatement. Vous pouvez appuyer sur le bouton pour interrompre la charge, ce qui s'appliquera instantanément.\

### Le menu du côté droit

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/SetupRed1.png){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------------- -------------------------------------------------------------
  ![image](icons/WifiBianco.PNG){height="8mm"}   

  ---------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------------- -------------------------------------------------------------
  ![image](icons/MQTTBianco.PNG){height="8mm"}   

  ---------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/ExitIcon2.png){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

# Configurations avancées de ToM+

## La page des paramètres Wi-Fi {#sec:wifi_settings}

Depuis la deuxième version du firmware, votre ToM+ peut désormais se connecter à Internet grâce à un module Wi-Fi intégré. Cela vous permettra de consulter les données en temps réel de votre Twizy si vous le combinez avec le protocole MQTT, qui sera traité dans la Section [4.2](#sec:MQTT){reference-type="ref" reference="sec:MQTT"}.\

<figure data-latex-placement="H">
<img src="figures/wifi_settings_3d.png" style="width:80.0%" />
<figcaption>La page des paramètres Wi-Fi.</figcaption>
</figure>

La page enregistrera jusqu'à quatre profils de connexion afin d'être connecté à Internet lorsque vous êtes à la maison, au travail ou dans un lieu public disposant d'un Wi-Fi gratuit.\
De plus, ToM+ dispose d'une interface web dans laquelle vous pouvez surveiller les données en temps réel ou personnaliser vos paramètres beaucoup plus facilement. Voyons maintenant pourquoi vous devriez faire cela...

### Avantages du Wi-Fi ToM+

Depuis la deuxième version du firmware, votre ToM+ peut désormais se connecter à Internet grâce à un module Wi-Fi intégré, ce qui vous permettra de débloquer beaucoup plus de fonctionnalités qu'auparavant. Vous pouvez désormais accéder aux données de votre Twizy à distance sur votre smartphone !\
Vous n'aurez plus besoin de vérifier manuellement l'état de charge de votre Twizy, car cette nouvelle fonctionnalité publiera les données de l'état de charge directement sur votre smartphone, de manière sécurisée et privée. Il suffira d'une simple configuration MQTT.\

- Fini la galère de devoir vérifier constamment l'état de charge de votre Twizy manuellement !

- De nombreuses possibilités d'intégrer votre Twizy dans un système IoT reposant sur MQTT

- Le Wi-Fi n'impacte presque pas la consommation électrique ni les performances de ToM

- Débloquez une nouvelle page web avec les données Twizy en temps réel et des paramètres ToM conviviaux

### Ajouter un profil de connexion Wi-Fi {#sec:add_wifi_profile}

Dans cette nouvelle page de paramètres, vous disposez d'un petit tableau avec quatre lignes et deux colonnes. La première colonne contient le **SSID** (c'est-à-dire le nom) du réseau auquel vous essayez de vous connecter. Pour être clair, c'est celui que vous voyez sur votre téléphone ou votre ordinateur portable. Il peut être alphanumérique et sensible à la casse (les majuscules comptent, assurez-vous donc de l'orthographier correctement !). La deuxième colonne, sous l'en-tête **« KEY »**, est destinée au mot de passe Wi-Fi.\
Lorsque vous appuyez sur une cellule du tableau, qu'il s'agisse du SSID ou de la clé, ToM+ ouvre une page de clavier sur laquelle vous pouvez saisir vos données. Appuyer sur OK confirmera la chaîne saisie et vous ramènera à la page des paramètres Wi-Fi. Nous aborderons la page du clavier dans la Section [4.3](#sec:keyboard_page){reference-type="ref" reference="sec:keyboard_page"}.\
Vous êtes désormais en mesure de configurer **quatre profils de connexion différents** avec quatre paires de SSID et de mots de passe. Si vous ne configurez aucun profil mais que les curseurs Wi-Fi sont activés, ToM+ effectuera tout de même une recherche Wi-Fi toutes les deux minutes pour essayer de trouver des connexions publiques sans protection par mot de passe, puis tentera de s'y connecter. Appuyez sur le bouton **flèche en bas à droite pour enregistrer**.\
Le quatrième profil de connexion Wi-Fi est spécial, car le champ **« KEY 4 »** sert à la fois de champ de mot de passe standard pour le dernier SSID et à modifier le mot de passe par défaut du serveur web, comme cela sera abordé dans la Section [4.4.3](#sec:web_change_password){reference-type="ref" reference="sec:web_change_password"}.

De plus, vous pouvez saisir certains codes spéciaux dans ce champ pour effectuer des configurations secrètes. Ces codes sont sensibles à la casse et n'affecteront pas votre champ **« KEY 4 »** s'ils sont écrits correctement, car ToM+ les utilise uniquement comme des commandes. Vous pouvez saisir **GIVEMEDF!** (exactement comme écrit ici, avec les tirets bas et le point d'exclamation) pour *afficher la numérotation et la description des erreurs DF* sur l'écran et sur l'interface webUI.\
**RAPPEL !** Les commandes ne sont exécutées par ToM+ que si elles sont saisies depuis cette page de paramètres Wi-Fi, et non depuis l'interface webUI abordée plus tard. De plus, l'origine du numéro DF n'étant pas claire, l'activation de cette fonction est à votre discrétion et sous votre responsabilité.

### Vérifier la connexion Wi-Fi {#sec:check_wifi_connection}

Pour vérifier si votre ToM+ est connecté à Internet via Wi-Fi, la procédure est très simple. Sur toutes les pages se trouve l'icône Wi-Fi (traitée dans la Section [3.3.3](#sec:status_icon_bar){reference-type="ref" reference="sec:status_icon_bar"}) qui indique son statut.

::: tcolorbox
  ------------------------------------------------ -------------------------------------------------------------
  ![image](icons/Tray_WiFiOff.png){height="8mm"}   

  ------------------------------------------------ -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/Tray_WiFi.png){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/Tray_WiFi.png){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

Si vous souhaitez obtenir des informations plus spécifiques pour savoir si votre ToM+ est connecté à un réseau, vous pouvez consulter des champs supplémentaires dans la page des paramètres Wi-Fi, dans le coin inférieur droit, comme illustré dans l'image ci-dessous.

<figure id="fig:wifi_bottom_line" data-latex-placement="H">
<img src="figures/wifi_bottom_line.png" style="width:70.0%" />
<figcaption>Informations de la grille inférieure Wi-Fi.</figcaption>
</figure>

Comme nous pouvons le voir, lorsque le ToM+ est connecté à un réseau, une adresse IP s'affiche (ici c'est **10.24.126.204**). Il s'agit de l'adresse prise par ToM+ pour se connecter à Internet. Si ce champ contient une séquence de quatre nombres (de 0 à 255) séparés par des points, le Wi-Fi est connecté ; sinon, il sera vide.

Appuyez dessus pour afficher l'adresse MAC de ToM+ et appuyez à nouveau pour voir à quel SSID (nom de réseau) ToM+ est connecté. Nous verrons d'autres fonctionnalités intéressantes impliquant l'adresse IP de ToM+ plus tard dans la Section [4.4.2](#sec:web_server_access){reference-type="ref" reference="sec:web_server_access"}.

### Activer/Désactiver les fonctionnalités Wi-Fi {#sec:enable_disable_wifi}

Dans le pied de page de la page des paramètres Wi-Fi, se trouvent deux boutons coulissants. Pour passer de l'état ON à OFF, il suffit de tapoter ou de faire glisser le bouton. Voyons ce que font ces deux curseurs.\
Le premier d'entre eux permet de désactiver le **Wi-Fi pendant la charge**. Cela rendra votre ToM+ complètement hors ligne, et vous ne pourrez plus surveiller les données de votre Twizy à distance tant que vous ne l'aurez pas réactivé. Dans cet état, l'icône de statut Wi-Fi sera toujours grisée, comme montré dans la Section [4.1.3](#sec:check_wifi_connection){reference-type="ref" reference="sec:check_wifi_connection"}.\
Le deuxième bouton coulissant permet d'activer le **Wi-Fi pendant la conduite**. Cela permettra à votre ToM+ de rester connecté à Internet même lorsque vous conduisez votre Twizy. C'est utile si vous souhaitez publier des données en temps réel sur votre smartphone via MQTT. Cela permet également d'accéder à l'interface web tout en conduisant, et votre ToM+ recherchera aussi les réseaux Wi-Fi disponibles.\
Comme déjà mentionné, pour *enregistrer vos modifications*, vous devez appuyer sur le bouton fléché en bas à droite. Si vous ne le faites pas, vos modifications seront perdues lorsque vous quitterez la page.

## La page des paramètres MQTT {#sec:MQTT}

Si vous avez déjà jeté un œil à la Section [4.1](#sec:wifi_settings){reference-type="ref" reference="sec:wifi_settings"} sur le Wi-Fi, vous savez probablement déjà que le MQTT est nécessaire pour accéder à vos données à distance. Cette section vous montrera comment le configurer correctement et comment l'interface ToM+ gère ce protocole.

<figure data-latex-placement="H">
<img src="figures/mqtt_settings_page.png" style="width:80.0%" />
<figcaption>La page des paramètres MQTT.</figcaption>
</figure>

Lorsque ToM+ est connecté à Internet via le Wi-Fi, le MQTT peut être activé pour vous permettre de consulter les données en temps réel de votre Twizy directement sur vos appareils. La page n'autorise qu'une seule configuration de serveur MQTT, afin de garantir la **sécurité et la confidentialité des données**. Vous pouvez configurer ces paramètres sur ToM+ ainsi que sur la page de son serveur web (Section [4.4.6](#sec:web_network_settings){reference-type="ref" reference="sec:web_network_settings"}). Présentons maintenant ce qu'est le MQTT et certains de ses principaux avantages...

### Brève explication du protocole MQTT {#sec:brief_mqtt}

Le MQTT est l'un des protocoles les plus simples utilisés en informatique pour communiquer de petits volumes de données en utilisant une **architecture client/serveur**. Cette méthode nécessite un ou plusieurs clients qui collectent généralement des données, souhaitent les stocker de manière permanente et/ou effectuer des calculs.

Le processus nécessite donc un serveur qui traite les données de tous les clients exécutant des tâches. Ce serveur est appelé **broker MQTT** ou couramment broker, et il est essentiel dans ce type d'architecture. Mais comment les clients et le serveur communiquent-ils entre eux ?\
Le processus de communication repose sur une structure de type publication/abonnement (publish/subscribe). Certains clients collectent et publient des données : ils sont appelés **éditeurs (publishers)**. Pendant ce temps, d'autres attendent que ces données soient envoyées : on les appelle les **abonnés (subscribers)**. Le serveur broker se situe au milieu et constitue le dispositif intermédiaire sur lequel toutes les données des éditeurs sont stockées et envoyées aux abonnés. Présentons maintenant les topics...\
Un **topic** est une séquence de caractères alphanumériques généralement liée à un sujet spécifique. Il est utilisé pour stocker (comme un conteneur) toutes les données relatives à ce sujet. Les topics sont utiles pour conserver et organiser une grande quantité de données collectées auprès de différents éditeurs afin de ne pas confondre ces informations. Alors, comment ToM+ utilise-t-il le MQTT ?

### Communications ToM+ et MQTT

Maintenant que nous savons ce qu'est le MQTT, voyons comment fonctionnent concrètement le système ToM+ et le MQTT. ToM+ est considéré comme un éditeur (publisher), car il collecte et publie les données mises à jour de la Twizy. L'application mobile, quant à elle, sera l'abonné (subscriber) puisqu'elle attend de recevoir les données que la Twizy vient de publier. Mais qui est au milieu ? Le serveur broker.\
À moins que vous ne disposiez d'un serveur broker auto-hébergé (comme c'est mon cas) ou que vous en connaissiez déjà un à utiliser, je vais vous expliquer comment configurer votre serveur broker externe gratuit dans la Section [4.2.3](#sec:free_broker){reference-type="ref" reference="sec:free_broker"}.

Ainsi, combiner ToM+ avec le protocole MQTT peut s'avérer très puissant et, si vous aimez la domotique et les systèmes IoT, cela peut également débloquer des possibilités infinies. Par exemple, vous pouvez créer votre propre abonné qui réalisera des actions sur les données publiées par ToM+.\

### Configuration d'un broker gratuit MQTT {#sec:free_broker}

*Avertissement* : Prenez votre temps lors de cette procédure, car pour les utilisateurs non expérimentés, cela peut prendre quelques minutes supplémentaires. Assurez-vous de bien **noter vos paramètres de configuration**.\
Tout d'abord, choisissez votre fournisseur de broker MQTT. Je recommande personnellement Maqiatto, car il est gratuit, intuitif et facile à utiliser. Visitons donc la page de tutoriel de leur site officiel : <https://www.maqiatto.com/examples>. Nous devrions maintenant voir une page semblable à celle présentée ici :

<figure data-latex-placement="H">
<img src="figures/mqtt_step1.png" style="width:100.0%" />
<figcaption>Étape 1 : Appuyez sur le bouton « CREATE ACCOUNT ».</figcaption>
</figure>

Comme l'indique le guide officiel, vous devez disposer d'un compte afin de créer votre broker MQTT. Appuyons donc sur le bouton entouré en haut à droite **« Create Account »** pour en créer un. Vous serez réorienté vers cette page (<https://www.maqiatto.com/signup>) où vous devrez remplir vos données personnelles.

<figure data-latex-placement="H">
<img src="figures/mqtt_step2.png" style="width:100.0%" />
<figcaption>Étape 2 : Remplissez vos données personnelles.</figcaption>
</figure>

Après avoir rempli tous les champs du formulaire, appuyez sur le bouton vert **« Signup »** et attendez d'obtenir cette page (<https://www.maqiatto.com/configure>) affichant un message de confirmation d'inscription, comme le montre l'image ci-dessous :

<figure id="sec:free_broker_add_topics" data-latex-placement="H">
<img src="figures/mqtt_step3.png" style="width:100.0%" />
<figcaption>Étape 3 : Ajoutez les topics IN/OUT.</figcaption>
</figure>

Depuis cette page, vous pouvez gérer vos topics disponibles (consultez la Section [4.2.1](#sec:brief_mqtt){reference-type="ref" reference="sec:brief_mqtt"}) et en créer de nouveaux. Créons donc nos topics IN et OUT pour envoyer et recevoir des données ToM. Comme nous pouvons le voir, il y a un préfixe fixe (votre adresse e-mail) car les utilisateurs gratuits ont cette limitation, mais ce n'est pas du tout un problème.\
Dans la zone de texte vide après le symbole « / », nous devons saisir le nom que nous souhaitons donner à nos topics. Choisissez-le soigneusement et assurez-vous qu'il soit clair et facile à retenir pour vous. Par exemple, j'appellerai le topic d'entrée **TOMin** et le topic de sortie **TOMout**, mais vous pouvez choisir le nom que vous préférez.\
Pour le premier topic, tapez **TOMin** et appuyez sur le bouton bleu **« + Add Topic »** comme je l'ai fait ci-dessus. Si l'opération réussit, un message vert s'affichera indiquant **« Topic was added for this user »** et un nouvel enregistrement apparaîtra dans la liste des *« Available Topics »* qui était vide auparavant. Répétez maintenant le processus pour le topic **TOMout** et vérifiez à nouveau s'il a bien été créé. Avant cette procédure, la liste des *« Available Topics »* était vide, mais nous pouvons désormais voir nos deux topics dans la liste et les supprimer si nécessaire.

<figure data-latex-placement="H">
<img src="figures/mqtt_step4.png" style="width:80.0%" />
<figcaption>Étape 4 : Modifiez le mot de passe de votre broker.</figcaption>
</figure>

*Cette étape est suggérée mais facultative*. À ce stade, le mot de passe du broker est le même que celui de votre compte Maqiatto et n'est pas du tout sécurisé. Mais si vous ne souhaitez pas le modifier ou si cela ne vous importe pas, vous pouvez ignorer cette étape et passer à la suivante.\
Prerenons donc le temps de sécuriser le broker afin de le protéger contre tout accès non autorisé. La seconde partie de cette page (<https://www.maqiatto.com/configure>) vous permet de modifier le mot de passe de votre broker. Saisissez simplement le nouveau mot de passe dans le champ texte **« New MQTT Password »**, puis appuyez sur le bouton bleu **« Change Password »**.

Si tout se passe bien, un message vert apparaîtra indiquant **« Broker user password was updated »**. Le bouton de modification du nom d'utilisateur est grisé car vous ne pouvez pas modifier votre nom d'utilisateur à moins d'être un utilisateur premium.

<figure data-latex-placement="H">
<img src="figures/mqtt_step5.png" style="width:70.0%" />
<figcaption>Étape 5 : Notez le numéro de port.</figcaption>
</figure>

Dans la dernière section de la page de configuration (<https://www.maqiatto.com/configure>), se trouvent les paramètres de **« Port Management »**. Notez le port TCP MQTT qui est généralement défini sur **1883** (juste pour être sûr), car il s'agit du numéro de port standard bien connu sur Internet pour le protocole MQTT. Le broker MQTT est désormais prêt à être utilisé et nous pouvons passer à l'étape suivante, qui consiste à configurer ToM+ avec les paramètres du broker.

### Connecter ToM+ au broker MQTT {#sec:mqtt_connection}

Maintenant que ce qu'est le MQTT est clair (Section [4.2.1](#sec:brief_mqtt){reference-type="ref" reference="sec:brief_mqtt"}) et que nous avons configuré notre broker personnel (Section [4.2.3](#sec:free_broker){reference-type="ref" reference="sec:free_broker"}), voyons où sur l'écran nous pouvons connecter ToM+ avec notre broker fraîchement créé.

<figure data-latex-placement="H">
<img src="figures/mqtt_connect1.png" style="width:80.0%" />
<figcaption>Paramètres de connexion au broker MQTT.</figcaption>
</figure>

Lorsque vous appuyez sur le champ correspondant du tableau, ToM+ ouvre une page de clavier sur laquelle vous pouvez saisir vos données, comme dans les paramètres Wi-Fi. Pour insérer les symboles ou les chiffres, appuyez sur le bouton **« 1/3 »** du clavier pour changer de jeu de caractères. En appuyant sur **OK**, vous confirmerez la chaîne saisie et cela vous ramènera à la page des paramètres MQTT. Pour en savoir plus sur la page du clavier, consultez la Section [4.3](#sec:keyboard_page){reference-type="ref" reference="sec:keyboard_page"}. Si la valeur est trop longue pour le champ, le texte défilera automatiquement.\
La première chose à spécifier est l'adresse de votre **broker**. Dans l'exemple présenté, elle est définie sur *« maqiatto.com »*. Il s'agit de l'adresse du serveur broker que nous venons de créer dans la Section [4.2.3](#sec:free_broker){reference-type="ref" reference="sec:free_broker"}.

Il faut ensuite spécifier le **numéro de port** sur lequel le service MQTT s'exécute. À moins que vous ne l'ayez modifié manuellement, le port MQTT sera toujours le *1883*.

Ensuite se trouve le champ **user**, qui correspond au nom d'utilisateur que ToM+ utilisera pour s'authentifier lors de la connexion au broker. La paire nom d'utilisateur et mot de passe étant unique pour vous, cela empêchera tout utilisateur indésirable d'accéder à votre broker privé. Dans votre cas, l'utilisateur est l'adresse e-mail de votre compte Maqiatto, écrite sous la forme *votreemail@example.com*.

Ensuite, nous devons spécifier le **mot de passe du broker**, qui peut être différent de celui de votre compte Maqiatto si vous avez choisi de le modifier lorsqu'il a été suggéré dans la Section [4.2.3](#sec:free_broker){reference-type="ref" reference="sec:free_broker"}.

<figure data-latex-placement="H">
<img src="figures/mqtt_connect2.png" style="width:80.0%" />
<figcaption>Paramètres de publication MQTT de ToM+.</figcaption>
</figure>

Configurons maintenant notre **topic OUT**, sur lequel ToM+ publiera les données de la Twizy. Dans la Section [4.2.3](#sec:free_broker){reference-type="ref" reference="sec:free_broker"}, nous avons créé un topic de sortie appelé TOMout, mais le nom complet du topic doit également inclure **votre e-mail comme préfixe** suivi d'un symbole « / » et du nom du topic « TOMout ». Dans l'exemple, il est défini sur *« votreemail@gmail.com/TOMout »*.

C'est maintenant au tour du **topic IN**, sur lequel ToM+ recevra les commandes MQTT. Comme pour le topic OUT, nous avons créé un topic d'entrée appelé TOMin, mais le nom complet du topic doit également inclure **votre e-mail comme préfixe** suivi d'un symbole « / » et du nom du topic « TOMin ». Dans l'exemple, il est défini sur *« votreemail@gmail.com/TOMin »*.

Lorsqu'un éditeur MQTT envoie un message au broker, sa connexion est authentifiée par nom d'utilisateur et mot de passe, mais il publie en utilisant un alias que *vous pouvez choisir arbitrairement*. Il est important de ne pas inclure d'espaces dans le **Client ID** : seuls les caractères alphanumériques et les symboles sont autorisés. N'oubliez pas qu'il est conseillé de le rendre simple et clair comme dans l'exemple : *« TwizOMeter »*.

Le dernier paramètre est la **fréquence de publication (publish frequency)**, qui représente l'intervalle de temps entre chaque publication de ToM+. Elle est exprimée en millisecondes *(ms)* et peut être définie sur une valeur arbitraire supérieure à 1000ms (une seconde). La valeur par défaut est de *5000 ms* (cinq secondes), ce qui constitue un bon compromis entre la fraîcheur des données et l'utilisation du réseau.\
Pour **enregistrer vos modifications**, vous devez appuyer sur le bouton fléché en bas à droite. Si vous ne le faites pas, vos modifications seront perdues lorsque vous quitterez la page. ToM+ est désormais prêt à publier et recevoir des données via le protocole MQTT.\

### Activer/Désactiver les fonctionnalités MQTT {#sec:enable_disable_mqtt}

Si vous souhaitez désactiver temporairement ou définitivement la publication de données avec le protocole MQTT, appuyez ou faites glisser le curseur de gauche appelé **« PUBLISH »** dans l'image ci-dessous. Dès lors, ToM+ ne publiera plus les données de la Twizy via MQTT tant que vous ne l'aurez pas réactivé.

<figure data-latex-placement="H">
<img src="figures/mqtt_connect3.png" style="width:80.0%" />
<figcaption>Curseurs inférieurs MQTT.</figcaption>
</figure>

Le bouton coulissant de droite sous **« SUBSCRIBE »** permet à ToM+ de recevoir des commandes provenant de périphériques externes publiées sur le topic IN spécifié. Cela est utile si vous souhaitez contrôler via MQTT un appareil connecté au port d'extension de ToM+ (par exemple, une prise connectée pour démarrer/arrêter la charge à distance). Vous pouvez choisir d'activer ou de désactiver cette fonctionnalité à tout moment en appuyant ou en faisant glisser le bouton.\

### Vérifier la connexion MQTT de ToM+

Près des deux boutons coulissants se trouve une petite étiquette **« STATUS »** qui indique si la connexion MQTT fonctionne ou non. Lorsque ToM+ est connecté au broker MQTT spécifié, le texte *« CONNECTED »* s'affiche. En cas de problème de connexion au broker ou si le Wi-Fi est désactivé, comme nous l'avons vu dans la Section [4.1.4](#sec:enable_disable_wifi){reference-type="ref" reference="sec:enable_disable_wifi"}, le protocole MQTT ne fonctionnera pas correctement et un message *« DISCONNECTED »* apparaîtra, comme sur l'image ci-dessous.

<figure data-latex-placement="H">
<img src="figures/mqtt_status.png" style="width:80.0%" />
<figcaption>Champ de statut MQTT.</figcaption>
</figure>

Par ailleurs, vous pouvez également vérifier le statut de la connexion MQTT en regardant la barre d'icônes de statut (Section [3.3.3](#sec:status_icon_bar){reference-type="ref" reference="sec:status_icon_bar"}) où l'icône MQTT sera violette si la connexion est établie, sinon elle sera grisée.

Pour **enregistrer vos modifications**, vous devez appuyer sur le bouton fléché en bas à droite. Si vous ne le faites pas, vos modifications seront perdues lorsque vous quitterez la page.\

## La page Clavier {#sec:keyboard_page}

Lorsque vous appuyez sur une cellule de tableau dans la page des paramètres Wi-Fi ou MQTT, ToM+ ouvre une page de clavier sur laquelle vous pouvez saisir vos données. La page de clavier est très intuitive et facile à utiliser. Vous pouvez basculer entre trois jeux de caractères différents en appuyant sur le bouton **« 1/3 »** dans le coin inférieur gauche du clavier.

<figure data-latex-placement="ht">
<figure>
<img src="figures/keyboard_page1.jpg" />
<figcaption>Premier jeu de caractères : Lettres.</figcaption>
</figure>
<figure>
<img src="figures/keyboard_page1_caps.jpg" />
<figcaption>Premier jeu de caractères : Majuscules.</figcaption>
</figure>
<figcaption>Premier jeu de caractères : Majuscules.</figcaption>
</figure>

Dans le **premier jeu de caractères**, vous pouvez saisir des lettres en minuscules ou en majuscules en appuyant sur le bouton majuscule entouré en jaune dans la première image. Lorsque vous saisissez quelque chose, cela apparaît dans le champ texte en haut du clavier. Si vous souhaitez supprimer un caractère, appuyez simplement sur la touche retour arrière.

<figure data-latex-placement="ht">
<figure>
<img src="figures/keyboard_page2.jpg" />
<figcaption>Deuxième jeu de caractères : Symboles.</figcaption>
</figure>
<figure>
<img src="figures/keyboard_page3.jpg" />
<figcaption>Troisième jeu de caractères : Chiffres et plus.</figcaption>
</figure>
<figcaption>Troisième jeu de caractères : Chiffres et plus.</figcaption>
</figure>

Le **deuxième jeu de caractères** est destiné aux symboles et le **troisième** aux chiffres et autres caractères spéciaux. Pour passer au troisième jeu de caractères, appuyez simplement sur le bouton **« 2/3 »** dans le coin inférieur gauche du clavier. Une fois sur le troisième jeu de caractères, vous pouvez revenir au premier en appuyant sur le bouton **« 3/3 »**. Sur ces deux pages, la touche majuscule ne fera rien car elle n'est pas nécessaire.\
Lorsque vous avez terminé la saisie, appuyez sur le bouton **OK** pour confirmer votre saisie et revenir à la page de paramètres MQTT ou Wi-Fi précédente, où le champ modifié sera mis à jour.

### Le clavier numérique uniquement

Dans certains champs, tels que la fréquence de publication MQTT, seuls les chiffres sont autorisés. Dans ce cas, ToM+ ouvrira une page de clavier numérique uniquement, comme montré dans l'image ci-dessous.

<figure data-latex-placement="H">
<img src="figures/keyboard_num_only.jpg" style="width:80.0%" />
<figcaption>Clavier numérique uniquement.</figcaption>
</figure>

Comme vous pouvez le constater, la disposition est la même que celle du troisième jeu de caractères du clavier complet, mais elle est limitée aux chiffres et à quelques caractères spéciaux. Vous pouvez également remarquer que le bouton de changement de jeu de caractères est indisponible, car il n'est pas nécessaire dans ce cas. La touche retour arrière reste disponible pour supprimer des caractères, et le bouton **OK** confirme votre saisie puis retourne à la page précédente.

## Le serveur web {#sec:web_server}

Le serveur web est une nouvelle fonctionnalité introduite avec la deuxième version du firmware. Il vous permet d'accéder aux paramètres et aux données de votre ToM+ à distance depuis n'importe quel appareil doté d'un navigateur web, comme votre smartphone, votre tablette ou votre PC. C'est particulièrement utile pour gérer les configurations standard et **avancées** qui ne sont pas disponibles sur l'écran du ToM+.

De plus, vous pouvez également utiliser le serveur web pour configurer le **Wi-Fi et le MQTT** bien plus facilement qu'en utilisant uniquement l'écran du ToM+ avec la page clavier (Section [4.3](#sec:keyboard_page){reference-type="ref" reference="sec:keyboard_page"}).\

<figure data-latex-placement="H">
<img src="figures/landing_page.png" style="width:46.0%" />
<figcaption>Page d’accueil du serveur web.</figcaption>
</figure>

### La page d'accueil

Sur la page d'accueil illustrée ci-dessus, vous verrez douze boutons qui vous donnent accès aux différentes pages du serveur web. Je vais donner ici un rapide aperçu des fonctions disponibles sur chaque page, puis elles seront toutes approfondies dans les paragraphes suivants. Dans cette section, les icônes ne servent qu'à titre d'aide visuelle :\

::: tcolorbox
  ------------------------------------------------ -------------------------------------------------------------
  ![image](icons/BatteryInfo2.png){height="8mm"}   

  ------------------------------------------------ -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------------ -------------------------------------------------------------
  ![image](icons/Street0Ok_v2.png){height="8mm"}   

  ------------------------------------------------ -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------------ -------------------------------------------------------------
  ![image](icons/Tray_WiFiOff.png){height="8mm"}   

  ------------------------------------------------ -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/Pin1.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------- -------------------------------------------------------------
  ![image](icons/Alarm.PNG){height="8mm"}   

  ----------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------- -------------------------------------------------------------
  ![image](icons/Alarm.PNG){height="8mm"}   

  ----------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/Swap.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/Swap.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/CEta.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------- -------------------------------------------------------------
  ![image](icons/Timer.PNG){height="8mm"}   

  ----------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------- -------------------------------------------------------------
  ![image](icons/Kmh.png){height="8mm"}   

  --------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------- -------------------------------------------------------------
  ![image](icons/Error.png){height="8mm"}   

  ----------------------------------------- -------------------------------------------------------------
:::

### Accéder au serveur web {#sec:web_server_access}

ToM+ vous permet de vous connecter à la page de son serveur web de deux manières, toutes deux utiles dans différentes situations. Avant de commencer, gardez à l'esprit qu'une **adresse IP** est fondamentalement le nom numérique de votre appareil sur un réseau (par ex. *192.168.1.100*).

***Pour les deux méthodes, vous devez connecter le ToM+ à un réseau.*** Assurez-vous donc de vérifier si votre ToM+ dispose d'un profil Wi-Fi configuré comme expliqué dans la Section [4.1.2](#sec:add_wifi_profile){reference-type="ref" reference="sec:add_wifi_profile"} ou s'il est connecté à un réseau Wi-Fi sans mot de passe. Pour vérifier si votre ToM+ est connecté, veuillez vous référer à la Section [4.1.3](#sec:check_wifi_connection){reference-type="ref" reference="sec:check_wifi_connection"}.\
**La première méthode, la plus simple,** consiste à utiliser le point d'accès (hotspot) de votre téléphone sans mot de passe, afin que ToM+ se connecte sans avoir à configurer de profil Wi-Fi. Ensuite, toujours avec votre téléphone, ouvrez Chrome ou Safari (ou n'importe quel navigateur web) et saisissez l'adresse IP de ToM+ (telle qu'illustrée sur la Figure [4.1](#fig:wifi_bottom_line){reference-type="ref" reference="fig:wifi_bottom_line"}).\
**La seconde méthode** ne fonctionne que si vous êtes assez proche de la Twizy, à portée du Wi-Fi. Vous pouvez utiliser votre téléphone ou votre ordinateur portable pour effectuer une recherche Wi-Fi, puis chercher le réseau *« ToM+ AP »*, *« Twiz o'Meter AP »* ou *« BigToM AP »*, selon votre modèle. Ensuite, connectez-vous à ce réseau avec le **bon mot de passe**. Il est initialement défini sur le mot « pass » suivi du numéro de série de votre appareil (par ex. *pass129777*). Le numéro de série se trouve sur la page des paramètres, comme expliqué dans la Figure [3.3](#fig:settings_page){reference-type="ref" reference="fig:settings_page"}. Vous pourrez ensuite le modifier si vous le souhaitez, mais il n'existe pas de système de récupération de mot de passe (voir Section [4.4.3](#sec:web_change_password){reference-type="ref" reference="sec:web_change_password"}). Une fois connecté au point d'accès de ToM+, saisissez son adresse IP statique sur n'importe quel navigateur, c'est-à-dire **192.188.1.188**.

### Changer le mot de passe du serveur web {#sec:web_change_password}

Pour modifier le mot de passe du serveur web, allez sur la page des paramètres Wi-Fi de l'écran (Section [4.1](#sec:wifi_settings){reference-type="ref" reference="sec:wifi_settings"}) et appuyez sur le champ **« KEY 4 »**. Cela ouvrira la page du clavier (Section [4.3](#sec:keyboard_page){reference-type="ref" reference="sec:keyboard_page"}) où vous pourrez saisir votre nouveau mot de passe. Ce mot de passe sera ainsi utilisé à la fois comme mot de passe du point d'accès et pour le quatrième profil de connexion Wi-Fi.

### Page du moniteur de données {#sec:web_data_monitor}

Comme indiqué dans l'introduction, cette page répertorie toutes les données ToM+ disponibles, organisées en sept tableaux différents dont chacun ne contient que les données spécifiées dans son en-tête. La répartition des données est la même que celle utilisée dans la Section [3.1](#sec:icon_list){reference-type="ref" reference="sec:icon_list"} et ne peut pas être modifiée.

Ces valeurs sont **mises à jour toutes les 10 secondes** et sont associées à leur unité de mesure. Ne vous inquiétez pas pour votre confidentialité car vos données voyagent encapsulées dans une structure de paquet particulière, difficile à intercepter ou à pirater. De plus, le serveur web n'utilise aucun service externe ni le protocole MQTT pour le contrôle, de sorte que vos données restent privées et sécurisées. La page est entièrement générée directement par le boîtier noir et ne subit aucun traitement ultérieur.

<figure data-latex-placement="H">
<img src="figures/monitor_page1.png" style="width:100.0%" />
<figcaption>Page du moniteur de données — tableaux supérieurs.</figcaption>
</figure>

Dans la deuxième partie de la page se trouvent les trois derniers tableaux contenant les données du tableau de bord, les données du port d'extension et le dernier réunit toutes les tensions et températures d'information de la batterie. Appuyez sur le bouton vert **« HOME »** pointé par la flèche rouge pour revenir à la page d'accueil.

<figure data-latex-placement="H">
<img src="figures/monitor_page2.png" style="width:100.0%" />
<figcaption>Page du moniteur de données — tableaux inférieurs.</figcaption>
</figure>

### Page de l'historique des trajets {#sec:web_trip_history}

Cette page contient les valeurs de la page des trajets précédemment abordée dans la Section [3.6](#sec:trip_page){reference-type="ref" reference="sec:trip_page"}. Elle peut stocker jusqu'à 5 ensembles de données différents et, même si les données affichées à l'écran sont limitées, la page du serveur web les montrera toutes. Le premier tableau présente les trajets, chacun organisé en cinq lignes, et les en-têtes de chaque enregistrement sont répertoriés dans la Section [3.1](#sec:icon_list){reference-type="ref" reference="sec:icon_list"}.

<figure data-latex-placement="H">
<img src="figures/trip_page1.png" style="width:100.0%" />
<figcaption>Page de l’historique des trajets — Données de trajet.</figcaption>
</figure>

Le deuxième tableau présente les vingt derniers trajets (du plus récent au plus ancien), avec les mêmes en-têtes que le premier tableau. Vous pouvez revenir à la page de démarrage en appuyant sur le bouton vert **« HOME »** situé juste sous le deuxième tableau.

<figure data-latex-placement="H">
<img src="figures/trip_page2.png" style="width:100.0%" />
<figcaption>Page de l’historique des trajets — Historique des trajets.</figcaption>
</figure>

### Page des paramètres réseau {#sec:web_network_settings}

Cette page vous permet de configurer les profils Wi-Fi et le broker MQTT sans avoir à utiliser le clavier de l'écran du ToM+. La page est divisée en deux tableaux principaux, l'un pour le Wi-Fi (Section [4.1](#sec:wifi_settings){reference-type="ref" reference="sec:wifi_settings"}) et l'autre pour les paramètres MQTT (Section [4.2](#sec:MQTT){reference-type="ref" reference="sec:MQTT"}).\
Comme vous pouvez le voir sur l'image, le premier contient les quatre profils précédemment configurés sur ToM+, ou à défaut, leurs valeurs par défaut. Il en va de même pour les mots de passe, qui ne sont pas visibles jusqu'à ce que vous appuyiez sur le bouton « O » situé à côté de celui que vous souhaitez afficher. Appuyer à nouveau dessus masquera le mot de passe. Vous pouvez également modifier ici le mot de passe Wi-Fi du point d'accès (Section [4.4.3](#sec:web_change_password){reference-type="ref" reference="sec:web_change_password"}).

<figure data-latex-placement="H">
<img src="figures/wifi_page1.png" style="width:100.0%" />
<figcaption>Page des paramètres réseau — Tableau Wi-Fi.</figcaption>
</figure>

Les deux cases à cocher remplissent les mêmes fonctions que les deux curseurs de la page des paramètres Wi-Fi du ToM+. Pour savoir à quoi ils servent, reportez-vous à la Section [4.1.4](#sec:enable_disable_wifi){reference-type="ref" reference="sec:enable_disable_wifi"}. Après toute modification, appuyez sur le bouton **« SAVE »** pour enregistrer vos changements, sinon ils seront perdus lorsque vous quitterez la page.

<figure data-latex-placement="H">
<img src="figures/wifi_page3.png" style="width:100.0%" />
<figcaption>Page des paramètres réseau — Tableau du statut Wi-Fi.</figcaption>
</figure>

Si votre ToM+ est connecté à un réseau, un petit tableau apparaîtra sous celui qui vient d'être décrit. Ses lignes contiennent trois informations principales : le SSID, l'adresse IP de ToM+ et l'adresse MAC. Ces données se trouvent également sur l'écran du ToM+, dans la page des paramètres Wi-Fi, comme montré précédemment sur la Figure [4.1](#fig:wifi_bottom_line){reference-type="ref" reference="fig:wifi_bottom_line"}.\
Le second tableau principal contient les paramètres du broker MQTT tels qu'ils ont été précédemment configurés sur l'écran du ToM+, ou à défaut leurs valeurs par défaut (*par ex. « broker.address »*). Vous pouvez facilement les modifier manuellement à partir de cette page du serveur web, ce qui est beaucoup plus confortable que d'utiliser le clavier de l'écran ToM+. Découvrez ci-dessous sur l'image à quoi ce tableau peut ressembler une fois configuré.

<figure data-latex-placement="H">
<img src="figures/wifi_page2.png" style="width:100.0%" />
<figcaption>Page des paramètres réseau — Tableau MQTT.</figcaption>
</figure>

Les deux cases à cocher remplissent les mêmes fonctions que les deux curseurs de la page des paramètres MQTT du ToM+. Pour savoir à quoi ils servent, reportez-vous à la Section [4.2.5](#sec:enable_disable_mqtt){reference-type="ref" reference="sec:enable_disable_mqtt"}. Si votre ToM+ est connecté au broker MQTT, l'en-tête du tableau affichera le texte **« (CONNECTED!) »**.\
Après toute modification, appuyez sur le bouton **« SAVE »** pour enregistrer vos changements, sinon ils seront perdus lorsque vous quitterez la page. Au bas de cette page, indiqué par une flèche rouge sur l'image, se trouve le bouton vert **« HOME »** pour revenir à la page d'accueil.

### Page des paramètres d'extension {#sec:web_expansion_settings}

Cette page contient la configuration des broches PIN1 et PIN2 du connecteur d'extension, ainsi que la configuration du bouton du commodo d'essuie-glace droit. Elle peut être très utile si vous aimez personnaliser des éléments et apporter votre touche personnelle à votre ToM+. Brochage du connecteur d'extension illustré sur la Figure [1.1](#fig:expansion_pinout){reference-type="ref" reference="fig:expansion_pinout"}. Puisqu'il s'agit de broches d'entrée/sortie générales, vous pouvez choisir le mode de chacune selon vos besoins.\
Si vous choisissez le mode **« INPUT »**, cette ligne écoutera le signal spécifié dans le champ suivant. Cela peut s'avérer très utile lors de la définition d'une alarme très spécifique, mais nous y reviendrons plus tard. D'autre part, si vous sélectionnez le mode **« OUTPUT »**, ToM+ transmettra le signal spécifié dans le champ suivant, qui peut être HIGH (5V) ou LOW (0V), lorsqu'une alarme se déclenche. Mais comme dit précédemment, ce point sera approfondi dans la Section [4.4.8](#sec:web_alarm_triggers){reference-type="ref" reference="sec:web_alarm_triggers"}.\
Depuis les versions de firmware les plus récentes, de nouveaux modes autres que INPUT et OUTPUT ont été ajoutés aux broches d'extension. Découvrons-les :\

- **IR CONTROLLER** : Ce mode permet de contrôler ToM+ par une télécommande infrarouge.

- **KEY+ CONTROLLER** : Ce mode vous permet de contrôler votre ToM+ via une télécommande rotative à infrarouge. Pour ces deux premiers modes, un tableau de configuration supplémentaire apparaîtra.

- **SERIAL TX** : Permet de configurer une ligne série TX (pas encore implémentée).

- **SERIAL RX** : Permet de configurer une ligne série RX (pas encore implémentée).

- **CTRL BUTTON** : Ce mode vous permet d'utiliser le bouton du commodo d'essuie-glace droit comme bouton de commande pour les gestes de votre ToM+.

#### Mode OUTPUT standard

Tant en mode **« OUTPUT »** qu'en mode **« INPUT »**, vous devrez tout d'abord choisir entre *« Active High »* et *« Active Low »*. Lorsqu'une alarme se déclenche, un signal LOW/HIGH est envoyé à la broche choisie comme sortie d'alarme (PIN1 ou PIN2).

Si vous sélectionnez *« Active High »*, le signal envoyé est HIGH (5V) et est normalement maintenu à LOW (0V).

Si vous sélectionnez *« Active Low »*, le signal envoyé est LOW (0V) et est normalement maintenu à HIGH (5V).

<figure data-latex-placement="H">
<img src="figures/expansion_page1.png" style="width:100.0%" />
<figcaption>Page des paramètres d’extension — Tableau PIN1.</figcaption>
</figure>

Comme vous pouvez le voir sur l'image ci-dessous, en sélectionnant le mode **« OUTPUT »**, vous pouvez également choisir le type de sortie *« Output Type »*. C'est utile si vous avez un périphérique de sortie très spécifique nécessitant une gestion supplémentaire qui ne se limite pas au signal standard HIGH/LOW. Pour cela, vous pouvez choisir parmi une liste de périphériques de sortie déjà gérés, mis en évidence sur l'image ci-dessus.\
Après toute modification, appuyez sur le bouton **« SAVE »** pour enregistrer vos changements, sinon ils seront perdus lorsque vous quitterez la page. Si vous avez une idée de nouveau périphérique de sortie pouvant être utile à la communauté, n'hésitez pas à me contacter.\

- *« Normal »* : C'est le mode OUTPUT standard, limité aux signaux HIGH/LOW.

- *« Charger auxilliary fan »* : Permet de contrôler un ventilateur auxiliaire. Vous devrez régler une alarme sur la température du chargeur avec un seuil. Ainsi, lors de la charge, si l'alarme se déclenche, le ventilateur commencera à refroidir le chargeur et ne s'arrêtera que lorsque la température repassera sous le seuil sélectionné avec une hystérésis fixe (même une fois la charge terminée si nécessaire).

- *« Reku break light »* : Permet de connecter une carte relais qui contrôle les feux stop afin de les allumer en mode régénération. C'est particulièrement utile si votre Twizy est préparée pour augmenter la puissance de régénération.

- *« Auxilliary charger »* : Permet de contrôler un chargeur auxiliaire avec une alarme sur le SOC ou la tension de batterie. Permet de connecter une carte relais qui active ou désactive un chargeur auxiliaire en cas de besoin. Il ne s'allume qu'en mode charge, avec un court délai fixe.

- *« Motor fan »* : Permet de contrôler un ventilateur moteur avec une alarme sur la température du moteur. Il fonctionne de la même manière que le ventilateur du chargeur, à la différence que celui-ci ne fonctionne que pendant la conduite.

#### Mode INPUT standard

Comme vous pouvez le voir sur l'image ci-dessous, lors de la sélection du mode **« INPUT »**, aucun tableau supplémentaire n'apparaît. Ce mode repose fortement sur la configuration et les déclencheurs d'alarme, veuillez donc vous référer à la Section [4.4.8](#sec:web_alarm_triggers){reference-type="ref" reference="sec:web_alarm_triggers"}. Nous avons choisi le mode **« INPUT »** dans le second tableau, qui fonctionne de la même manière mais est destiné à la broche PIN2 du connecteur d'extension.

Après toute modification, appuyez sur le bouton **« SAVE »** pour enregistrer vos changements, sinon ils seront perdus lorsque vous quitterez la page.

<figure data-latex-placement="H">
<img src="figures/expansion_page3.png" style="width:100.0%" />
<figcaption>Page des paramètres d’extension — Tableau PIN2.</figcaption>
</figure>

#### Mode IR CONTROLLER

Tout d'abord, vous aurez besoin d'un récepteur IR (soit un capteur, soit un module comme celui de la première image) à brancher sur l'une des broches de la carte d'extension. Ce mode est destiné à être utilisé avec une télécommande IR générique, mais celle que je suggère personnellement est celle montrée sur la deuxième image ci-dessous, spécialement conçue pour être installée sur le volant.

<figure data-latex-placement="ht">
<figure>
<img src="figures/ir_receiver.jpg" />
<figcaption>Module récepteur IR.</figcaption>
</figure>
<figure>
<img src="figures/ir_controller_photo.jpg" />
<figcaption>Télécommande IR de volant.</figcaption>
</figure>
<figcaption>Télécommande IR de volant.</figcaption>
</figure>

Lorsque vous sélectionnez le mode **« IR CONTROLLER »** pour le tableau de la broche PIN1 ou PIN2, n'oubliez pas d'appuyer sur le bouton **« SAVE »** pour enregistrer vos modifications. Une fois enregistré, la page se rechargera et un tableau supplémentaire apparaîtra en dessous, visible sur l'image ci-dessous.

<figure data-latex-placement="H">
<img src="figures/ir_settings.png" style="width:80.0%" />
<figcaption>Page des paramètres d’extension — Tableau des réglages IR.</figcaption>
</figure>

Ce tableau vous aidera à associer chaque bouton de la télécommande IR avec le code IR correspondant. Dans la partie supérieure du tableau, il y a une zone de texte que vous pouvez utiliser comme **moniteur de récepteur de code IR** pour tester en temps réel les codes IR de votre télécommande après avoir branché le récepteur IR.\
Grâce à cela, vous pouvez remplir les autres champs en conséquence. Le dernier est particulièrement important : c'est le code que la télécommande envoie lorsque vous maintenez un bouton enfoncé. Ensuite, n'oubliez pas d'appuyer sur le bouton **« SAVE »** pour enregistrer vos modifications, sinon elles seront perdues en quittant la page. Enfin, un bouton pratique **« Default »** est situé à côté pour rétablir facilement vos modifications si nécessaire.

#### Mode KEY+ CONTROLLER

Ce mode est très similaire à celui qu'on vient de décrire, mais il est destiné à être utilisé avec un autre type de commande (celui présenté sur la photo ci-dessous). Il s'agit d'une commande rotative sans fil Bluetooth pour systèmes audio embarqués, qui effectue différentes actions en fonction de la vitesse à laquelle vous tournez la bague externe. Et bien sûr, elle possède aussi d'autres boutons sur la partie interne.\

<figure data-latex-placement="H">
<img src="figures/keyp_controller.jpg" style="width:40.0%" />
<figcaption>Commande rotative sans fil Bluetooth.</figcaption>
</figure>

Lorsque vous sélectionnez le mode **« KEY+ CONTROLLER »** pour le tableau PIN1 ou PIN2, pensez à appuyer sur le bouton **« SAVE »** pour enregistrer vos modifications. Une fois enregistré, la page se rechargera et un tableau supplémentaire apparaîtra ci-dessous, vous pouvez le voir sur l'image ci-dessous.

<figure data-latex-placement="H">
<img src="figures/keyp_settings.png" style="width:80.0%" />
<figcaption>Page des paramètres d’extension — Tableau des réglages KEY+.</figcaption>
</figure>

Cela fonctionne de la même manière que le tableau des paramètres IR. La différence majeure réside dans ce que ToM+ lit depuis le port d'extension : il ne s'agit plus d'un code IR, mais d'une tension.

Dans l'image ci-dessus sont affichées les valeurs par défaut, allant de *0* à *3.3V* écrites sans la virgule décimale. Par exemple, *018* signifie *0.18V* et *157* signifie *1.57V*, et ainsi de suite. ToM+ a une tolérance de *0.05V* sur les valeurs d'entrée afin d'éviter les rebonds de tension.\
Après cela, n'oubliez pas d'appuyer sur le bouton **« SAVE »** pour enregistrer vos modifications, sinon elles seront perdues quand vous quittiez la page. Enfin, un bouton utile **« Default »** est situé juste à côté pour annuler facilement vos changements au besoin.

#### Mode CTRL BUTTON {#sec:web_wiper_stalk}

Ce dernier tableau contient la configuration nécessaire pour faire fonctionner le **bouton du commodo d'essuie-glace droit** fourni (Figure [1.4](#fig:wiper_stalk_button){reference-type="ref" reference="fig:wiper_stalk_button"}). Vous pouvez utiliser ce bouton pour naviguer dans toute l'interface ToM+ sans utiliser l'écran tactile, grâce à ces trois **actions** principales : *« Browse items »* (Parcourir les éléments), *« Change page »* (Changer de page), *« Select-deselect »* (Sélectionner-désélectionner). Pour ce faire, il existe trois types d'**appuis sur le bouton** : *« Short »* (Court), *« Medium »* (Moyen), *« Long »* (Long).\

<figure data-latex-placement="H">
<img src="figures/expansion_page2.png" style="width:100.0%" />
<figcaption>Page des paramètres d’extension — Tableau du bouton d’essuie-glace.</figcaption>
</figure>

Ainsi, dans la première partie de ce tableau, vous pouvez réorganiser ces actions avec les gestes de votre choix.\

- *« Browse items »* : Déplace un petit marqueur blanc à côté de la donnée actuellement sélectionnée.

- *« Change page »* : Permet de faire défiler les pages présentes dans la boucle.

- *« Select-deselect »* : Simule un appui sur la donnée sélectionnée (ex. passe de l'arrière-plan au premier plan).\

Dans la deuxième partie du tableau, vous pouvez sélectionner les **pages que vous souhaitez ignorer** lors du défilement des pages disponibles en répétant le geste *« Change page »*. Par exemple, si je ne souhaite pas surveiller la page d'info batterie lors du défilement avec le bouton, il me suffit de la décocher pour qu'elle soit retirée de la boucle.\
Après toute modification, appuyez sur le bouton **« SAVE »** pour enregistrer vos changements, sinon ils seront perdus lorsque vous quitterez la page. Au bas de cette page, indiqué par une flèche rouge sur l'image, se trouve le bouton vert **« HOME »** pour revenir à la page d'accueil.

### Page des déclencheurs d'alarme {#sec:web_alarm_triggers}

Lorsque quelque chose se produit sur ToM+ et que vous souhaitez en être notifié, vous pouvez choisir comment être averti et quand dans cette page. Vous pouvez avoir jusqu'à **dix alarmes** fonctionnant simultanément et ToM+ vérifie en permanence l'état de chaque condition. L'image montre le premier tableau, où vous pouvez voir les alarmes actuellement actives.

<figure data-latex-placement="H">
<img src="figures/alarm_page1.png" style="width:100.0%" />
<figcaption>Page d’alarme — Tableau de la liste des alarmes existantes.</figcaption>
</figure>

Les en-têtes des tableaux sont concrètement les éléments de la condition écoutés par ToM+.\

- **ITEM** : C'est la donnée à vérifier, choisie dans la liste de la Section [3.1](#sec:icon_list){reference-type="ref" reference="sec:icon_list"}.

- **CONDITION** : C'est le signe opérateur utilisé lors de la comparaison des valeurs.

- **VALUE** : C'est une valeur entière signée utilisée comme second terme de la comparaison.

- **ACTION** : C'est l'action exécutée lorsque l'alarme se déclenche. Voir le tableau suivant.

- **SEND-MQTT** : C me champ binaire et, s'il est coché, publie un message sur le topic MQTT.

- **COMMAND** : C'est une chaîne de caractères facultative à envoyer en tant que commande supplémentaire.

 \
Le premier déclencheur d'alarme vérifie la consommation de la batterie et active la broche PIN2 de la carte d'extension si elle est supérieure à 35A. Dans cet exemple spécifique, il sert à allumer le feu stop arrière lorsque la régénération est suffisante pour faire ralentir la Twizy.\
Le deuxième déclencheur d'alarme vérifie le SOC de la batterie et affiche sur l'écran une simple fenêtre contextuelle notifiant que le niveau de batterie est inférieur à 30 %. En cochant le champ *« Change page »*, j'ai ajouté une option supplémentaire qui demandera à ToM+ d'envoyer un message MQTT lorsque cette alarme se déclenche.\
Le troisième déclencheur d'alarme vérifie le SOC de la batterie et une fois la charge terminée (par exemple égale à 97 %), il fait la même chose qu'auparavant mais exécute une commande supplémentaire. La commande *cmd/charge/Power 0* désactive un interrupteur Wi-Fi Tasmota qui relie la prise de la Twizy à la prise murale.

La fonction de la colonne **« COMMAND »** est donc très utile et vous permet d'intégrer votre ToM+ dans votre maison connectée. Consultez l'Annexe [7](#apx:tasmota){reference-type="ref" reference="apx:tasmota"} pour des configurations détaillées.\
Lorsque vous souhaitez supprimer une alarme spécifique, il vous suffit d'appuyer sur le bouton **« Remove »** dans sa dernière colonne.\

<figure data-latex-placement="H">
<img src="figures/alarm_page2.png" style="width:100.0%" />
<figcaption>Page d’alarme — Tableau d’ajout d’une nouvelle alarme.</figcaption>
</figure>

Dans le deuxième tableau, vous pouvez ajouter une nouvelle alarme à la liste qu'on vient d'évoquer. Tout d'abord, vous devez choisir l'**ITEM**, parmi toutes les données disponibles listées dans la Section [3.1](#sec:icon_list){reference-type="ref" reference="sec:icon_list"}. Dans cette zone de choix, les éléments sont organisés comme dans la liste citée. Sélectionnez ensuite la **CONDITION**, c'est-à-dire l'opérateur de la comparaison, entre *« lower »* (inférieur), *« greater »* (supérieur) ou *« equal »* (égal). Vient ensuite le moment de saisir la valeur de référence **VALUE**, un nombre entier signé qui constitue le terme de droite de la comparaison.\
Prenons le temps d'expliquer toutes les **ACTION**s possibles.\

- *pop-up* : une fenêtre contextuelle jaune notifiant la valeur de l'élément apparaît au centre de l'écran. Pour la masquer, appuyez dessus une fois. Vous pouvez voir un exemple de pop-up sur la première image ci-dessous.

- *pop-up 10 sec* : une fenêtre pop-up jaune notifiant la valeur de l'élément reste à l'écran pendant dix secondes.

- *silent* : aucune action visible n'a lieu : c'est généralement utilisé uniquement pour publier des messages MQTT.

- *icon x fix* : l'icône x (*où x peut être 2, 3, 4 ou 5*) s'allume. Voir la Figure [4.4](#fig:alarm_icons2){reference-type="ref" reference="fig:alarm_icons2"} pour les icônes d'alarme.

- *icon x blink* : l'icône x (*où x peut être 2, 3, 4 ou 5*) commence à clignoter.

- *pin1 active* : la broche PIN1 de la carte d'extension s'active (LOW ou HIGH selon le niveau sélectionné sur la page des paramètres d'extension dans la Section [4.4.8](#sec:web_alarm_triggers){reference-type="ref" reference="sec:web_alarm_triggers"}).

- *pin2 active* : la broche PIN2 de la carte d'extension s'active. Dans cet exemple, PIN2 a été configurée en mode INPUT, elle est donc grisée car elle ne peut pas représenter une action OUTPUT.

 \

<figure id="fig:alarm_icons2" data-latex-placement="ht">
<figure>
<img src="figures/pop-up.PNG" />
<figcaption>Pop-up : Température batterie &gt; 89°C.</figcaption>
</figure>
<figure id="fig:alarm_icons2">
<img src="figures/alarm_icons.png" />
<figcaption>Icônes d’alarme (2, 3, 4 et 5).</figcaption>
</figure>
<figcaption>Icônes d’alarme (2, 3, 4 et 5).</figcaption>
</figure>

Le champ suivant est le drapeau binaire **SEND MQTT** : s'il est activé, ToM+ publie un message MQTT sur le topic OUT MQTT configuré (ex. TOMout, voir Section [4.2.4](#sec:mqtt_connection){reference-type="ref" reference="sec:mqtt_connection"}) lorsque l'alarme se déclenche en guise de notification supplémentaire. Enfin, le champ texte **AUX CMD** contient une commande supplémentaire à envoyer via MQTT à d'autres appareils IoT. Voir l'Annexe [7](#apx:tasmota){reference-type="ref" reference="apx:tasmota"} pour les configurations détaillées d'un interrupteur Tasmota à titre d'exemple.\
Enfin, vous pouvez ajouter votre alarme en appuyant sur le bouton **« Add to list »**. La page se recharge automatiquement et le déclencheur d'alarme est ajouté à la liste du premier tableau.

Appuyez sur le bouton vert **« HOME »** en bas de la page pour revenir à la page d'accueil.

### Page du journal des alarmes {#sec:web_alarms_log}

Cette page enregistre les 21 derniers déclenchements d'alarme et remplit la même fonction que la page de journal de ToM, comme présenté dans la Section [3.5](#sec:alarm_log){reference-type="ref" reference="sec:alarm_log"}. Vous pouvez également consulter et supprimer tout enregistrement indésirable en appuyant sur le bouton **« Remove »** situé près de celui que vous souhaitez supprimer définitivement (sur l'écran ToM+ également).\

<figure data-latex-placement="H">
<img src="figures/alarm_log1.png" style="width:60.0%" />
<figcaption>Tableau de la page du journal des alarmes.</figcaption>
</figure>

Évidemment, le tableau contient l'**ITEM** et la valeur **VALUE** qui ont déclenché l'alarme. Des champs supplémentaires indiquent également la date et l'heure auxquelles le déclenchement s'est produit. Ensuite, comme d'habitude, appuyez sur le bouton vert **« HOME »** en bas de page pour revenir à la page d'accueil.

### Page des mises à jour OTA & Préférences {#sec:web_ota_update}

Dans cette page, vous pouvez **mettre à jour le firmware** à la volée depuis l'interface web, sans avoir à vous battre avec l'outil de flashage comme sur les anciennes versions. Cette nouvelle fonctionnalité fait gagner du temps et s'avère bien plus conviviale : veillez donc à toujours avoir la dernière version du firmware installée pour accéder aux fonctionnalités et améliorations les plus récentes !

#### Mise à jour OTA

Le premier tableau vous donne des informations sur le firmware du boîtier noir (blackbox) : analysons ces valeurs. Le **ESP fw** est probablement l'élément le plus important de la grille car il vous indique la version actuellement installée et chargée sur la carte mère ESP.

Un autre champ utile est le **S/N** qui signifie numéro de série (Serial Number), que vous pouvez également trouver sur ToM+ comme vu sur la Figure [3.3](#fig:settings_page){reference-type="ref" reference="fig:settings_page"}. La ligne suivante est un peu plus technique et est directement liée au mécanisme de mise à jour OTA (Over-The-Air). **Current ptn** et **Next ptn** font référence aux adresses de partition où le firmware est actuellement stocké et où il sera stocké pendant que la mise à jour est en cours.\
Parfois, des correctifs de firmware (comme des corrections de bugs ou des ajustements mineurs) peuvent être publiés sans changer le numéro de version (ex. 2.4). Dans ces cas-là, il peut être utile de connaître le fichier binaire spécifique installé, c'est pourquoi les deux champs suivants contiennent son nom complet. Comme vous pouvez le constater, il existe deux partitions principales de firmware, **Ota0** et **Ota1**, afin que vous puissiez avoir deux versions différentes installées et passer de l'une à l'autre au besoin. Ici, le nom complet est *ESP32_Fw24_70_4error12* pour les deux.

Le dernier champ correspond au nom complet du firmware de la **Special partition**, qui est un stockage supplémentaire utilisé pour accueillir des logiciels tiers (ex. le logiciel de réglage Twizy-cfg). Pour plus d'informations sur la modification de votre Twizy avec Twizy-cfg sur ToM+, reportez-vous à l'Annexe [6](#apx:tuning){reference-type="ref" reference="apx:tuning"}.

<figure data-latex-placement="H">
<img src="figures/ota_page3.png" style="width:100.0%" />
<figcaption>Page de mise à jour OTA — Tableau de mise à jour et d’informations.</figcaption>
</figure>

La deuxième partie de ce tableau vous permet de mettre à jour le firmware ou de charger un logiciel tiers. Tout d'abord, téléchargez le fichier binaire (avec l'extension .bin) que vous souhaitez installer sur ToM+. Appuyez ensuite sur le bouton **« Browse...»** et parcourez les dossiers de votre appareil jusqu'à trouver le fichier désiré.

S'il s'agit d'une *mise à jour ToM+ standard*, appuyez directement sur le bouton **« UPDATE »**. Pour suivre l'avancement de la mise à jour, une barre de progression orange apparaît en bas du tableau avec son pourcentage. Lorsqu'elle atteint 100 %, ToM+ redémarrera pour appliquer les modifications.

S'il s'agit d'un *logiciel tiers*, veillez à cocher l'option *« Update to special partition »* et, seulement après cela, appuyez sur le bouton **« UPDATE »**. Dès que la mise à jour est terminée, ToM+ redémarre et charge le firmware de la partition spéciale.\
Dans le tableau **« BOOT OPTIONS »**, une fois les firmwares souhaités chargés, vous pouvez basculer de l'un à l'autre en cas de besoin. Admettons que j'exécute le firmware ToM+ 2.4 et que je souhaite faire des réglages avec le logiciel tiers Twizy-cfg ; j'ai déjà chargé les deux dans les partitions appropriées. Pour ce faire, appuyez sur le bouton *« Reboot from special partition »* et attendez que ToM+ redémarre, puis suivez l'Annexe [6](#apx:tuning){reference-type="ref" reference="apx:tuning"} pour la suite.\
Les boutons *« Reboot from Ota0 partition »* et *« Reboot from Ota1 partition »* permettent de basculer entre les versions du firmware ToM+. Supposons que j'utilise le firmware ToM+ 2.4 mais que, pour une raison quelconque, je souhaite revenir à la version 2.3 que j'avais auparavant. Pour cela, appuyez sur le bouton correspondant pour redémarrer depuis Ota1 ou Ota0. ToM+ redémarrera immédiatement et vous serez déconnecté de l'interface web.

<figure data-latex-placement="H">
<img src="figures/ota_boot.png" style="width:100.0%" />
<figcaption>Page de mise à jour OTA — Tableau des options de démarrage.</figcaption>
</figure>

En passant au tableau suivant, nous avons le tableau **« LCD FIRMWARE UPDATE »**, qui permet également d'effectuer des mises à jour OTA pour l'écran LCD. Cela signifie qu'il n'y a plus besoin de s'embêter avec la carte microSD et le petit trou sur l'écran.\
**AVERTISSEMENT :** Comme indiqué dans le tableau, vous **NE DEVEZ PAS** fermer cette page web pendant la mise à jour : il est conseillé de désactiver votre écran de veille pour éviter tout échec de la mise à jour. Le processus peut prendre quelques minutes, selon la version du firmware, jusqu'à 10 minutes.\
La procédure est similaire à la mise à jour OTA du boîtier noir. Tout d'abord, téléchargez le fichier (avec l'extension .tft) que vous souhaitez installer sur ToM+. Appuyez ensuite sur le bouton **« Browse...»** et parcourez les dossiers de votre appareil pour trouver le fichier souhaité.

Si vous *mettez à jour l'écran principal*, appuyez sur le bouton **« UPDATE LCD »**. Pour suivre l'état de la mise à jour, la barre de progression bleue sous l'encadré d'avertissement affichera les blocs copiés vers l'écran LCD. Lorsqu'elle sera terminée, l'écran redémarrera (et non le boîtier noir).

Si vous *mettez à jour l'écran secondaire (twin display)*, veillez à cocher l'option *« Update AUX LCD »* et, seulement après, appuyez sur le bouton **« UPDATE LCD »**. Dès que la mise à jour est terminée, l'écran LCD redémarre et charge le firmware souhaité.

<figure data-latex-placement="H">
<img src="figures/ota_lcd.png" style="width:100.0%" />
<figcaption>Page de mise à jour OTA — Tableau de mise à jour du firmware LCD.</figcaption>
</figure>

#### Préférences et mise à niveau matérielle

Dans la section suivante de la page web, nous pouvons gérer les préférences, ce qui inclut les configurations Wi-Fi et MQTT, l'organisation des icônes de pages ToM+, et bien plus encore. Il est donc toujours conseillé d'effectuer une **sauvegarde avant de mettre à jour**, afin d'éviter de devoir ressaisir vos mots de passe si une mise à jour se passe mal. Pour ce faire, appuyez sur le bouton **« BACKUP »** et un fichier nommé *prefs.ToM* sera téléchargé sur votre appareil. Parfois, une fenêtre pop-up s'ouvre pour vous avertir que ce fichier a une extension inhabituelle : cliquez sur le bouton *Conserver* et téléchargez-le quand même.\
Le processus inverse est tout aussi simple. Appuyez sur le bouton **« Browse...»** et parcourez les dossiers de votre appareil jusqu'à trouver le fichier de préférences *prefs.ToM*. Pour appliquer les modifications, appuyez sur le bouton **« RESTORE »** et vous serez réorienté vers la page d'accueil pour confirmation.

<figure data-latex-placement="H">
<img src="figures/prefs_page.png" style="width:100.0%" />
<figcaption>Page de mise à jour OTA — Tableau de sauvegarde des préférences.</figcaption>
</figure>

Ce tableau suivant est très spécifique aux utilisateurs des anciennes versions de ToM qui ont maintenant reçu le mot de passe pour mettre à niveau leur appareil vers ToM+ sans changer le boîtier noir. Si c'est votre cas, veuillez saisir le mot de passe dans le champ texte et appuyer sur le bouton **« UPGRADE »**. Dès lors, votre ToM est enfin mis à niveau vers ToM+, profitez-en !

<figure data-latex-placement="H">
<img src="figures/hw_upgrade.png" style="width:100.0%" />
<figcaption>Page de mise à jour OTA — Tableau de mise à niveau matérielle.</figcaption>
</figure>

Appuyez sur le bouton vert **« HOME »** en bas du tableau pour revenir à la page d'accueil.

### Page des infos et réglages avancés {#sec:web_advanced_info}

Cette page est destinée à divers réglages avancés qui ne sont pas disponibles dans les pages de paramètres d'affichage du ToM+ abordées dans la Section [3.10](#sec:settings_page){reference-type="ref" reference="sec:settings_page"} pour des raisons d'espace.\
La première case, **« Disable Auto-dimming »**, peut être cochée si vous ne souhaitez pas que l'écran LCD de ToM+ adapte sa luminosité lors de l'allumage des feux. Sinon, vous pouvez régler la luminosité de variation **« Dimming brightness (%) »** exprimée en pourcentage (jusqu'à 100 %), et définir vous-même le facteur de réduction de luminosité lorsque les feux sont activés.

<figure data-latex-placement="H">
<img src="figures/adv_sett_page1.png" style="width:100.0%" />
<figcaption>Page des infos avancées — Tableau des paramètres avancés.</figcaption>
</figure>

Ensuite, nous trouvons la sous-section **Warning messages at power-off** (messages d'avertissement à l'extinction), où vous pouvez sélectionner les rappels (*feux* et *frein à main*) et informations (*erreurs système* et *limites de charge*) affichés sur la fenêtre pop-up d'extinction de ToM+. Cela ressemble à l'image ci-dessous, vous informant par exemple si vous avez oublié d'engager le frein à main. Les deux dernières cases à cocher sont réservées à des usages futurs et ne sont pas encore implémentées.

<figure data-latex-placement="H">
<img src="figures/pop-up_finale.png" style="width:50.0%" />
<figcaption>Message d’avertissement à l’extinction.</figcaption>
</figure>

Puis, il y a le champ **« Secondary font colour »** avec un sélecteur de couleur, utilisé pour changer la couleur de la police secondaire sur l'écran du ToM+.

Une autre case disponible est **« Invert current value sign »**. Si elle est cochée, elle affiche un entier signé pour les valeurs de consommation de courant au lieu de leurs valeurs absolues.\
Le petit sous-groupe ci-dessous est dédié à la compatibilité du **Cheatzy** avec ToM+. Vous pouvez régler votre facteur de triche **« Cheating factor »** multiplié par 10 : par exemple, 2.0 devient 20. Vous pouvez également sélectionner si le Cheatzy est activé pendant la charge ou lors du freinage régénératif à l'aide de la case **« Cheat also Charge/Reku »**. Ces réglages n'ont de sens que si le Cheatzy est connecté et allumé, sinon ils risquent d'altérer vos valeurs de courant de manière incorrecte.\
Ensuite, se trouve une autre option : **« Increase thermal protection threshold »**, utilisée pour augmenter de 15°C le seuil de sécurité de surchauffe pour ToM+ durant les saisons les plus chaudes.

Les deux valeurs suivantes sont des configurations supplémentaires pour le calcul du kilométrage restant **Remaining KM** de ToM+, basé sur l'échantillonnage de la consommation récente. Ici, vous pouvez ajuster la fréquence de l'échantillonnage (par défaut : un par minute) dans **« Remaining KM sampling time (min) »** et la part du dernier échantillon dans le calcul total (par défaut : 10 %) dans **« Remaining KM sample weight (%) »**.\
Enfin, nous avons la case **« Miles to Kilometers »**, qui aide lorsque votre BigToM est issu d'un tableau de bord en miles mais que vous souhaitez le km/h comme unité de mesure. Si elle est activée, ToM+ effectuera cette conversion pour vous.

Pensez à **enregistrer vos modifications** en appuyant sur le bouton **« SAVE »** au bas de ce tableau. Si vous ne le faites pas, vos modifications seront perdues lorsque vous quitterez la page.

<figure data-latex-placement="H">
<img src="figures/adv_info.png" style="width:90.0%" />
<figcaption>Page des infos avancées — Tableau des infos avancées.</figcaption>
</figure>

Le tableau ci-dessus contient des données relatives à votre batterie, telles que la capacité stockée, la santé **SOH**, le **kilométrage de la batterie**, le total de kWh consommés, ainsi que sur les charges, comme le nombre de charges *totales*, *complètes* et *partielles*, et la **puissance de charge maximale acceptée**.\

<figure data-latex-placement="H">
<img src="figures/item_scroll.png" style="width:100.0%" />
<figcaption>Page des infos avancées — Tableau du défilement des éléments.</figcaption>
</figure>

Ce dernier tableau est une fonctionnalité très particulière introduite il y a quelques mises à jour, qui vous permet d'avoir des éléments qui changent dynamiquement dans les pages de votre choix. Cela peut s'appliquer aux pages *batterie*, *moteur*, *gyroscope*, *trajet* et *charge*, et vous pouvez choisir laquelle grâce au champ **« Page »**.

Ensuite, vous pouvez sélectionner l'emplacement où vous souhaitez faire défiler les éléments de données de votre choix. Pour cela, utilisez le champ **« Position »** et choisissez dans la liste celui que vous préférez, en vous référant à la Figure [3.4](#fig:icon_arrangement){reference-type="ref" reference="fig:icon_arrangement"} pour la disposition des éléments.\
Le champ **« Freq »** correspond à la fréquence de défilement, c'est-à-dire le temps pendant lequel chaque donnée reste affichée à cet emplacement avant de passer à la suivante. Comme vous pouvez le remarquer, il est spécifié entre parenthèses que le champ sera multiplié par *5 secondes*. Cela signifie que la saisie de la valeur *1* entraînera une fréquence de *5 secondes*, la valeur *2* entraînera une fréquence de *10 secondes*, et ainsi de suite.

La partie la plus importante consiste à choisir les éléments à faire défiler : vous pouvez sélectionner jusqu'à dix valeurs de données. Dans les zones de texte **« Scrolling items »**, insérez la liste des numéros d'éléments souhaités (par ex. 59 ou 48), un par zone, en vous référant aux numéros entre parenthèses dans la liste de la Section [3.1.2](#sec:item_numbers){reference-type="ref" reference="sec:item_numbers"}.\
Pensez toujours à enregistrer vos modifications en appuyant sur le bouton **« SAVE »** en bas de ce tableau. Si vous ne le faites pas, vos modifications seront perdues quand vous quitterez la page.

Si vous souhaitez **désactiver** la fonction de défilement pour une page et une position spécifiques, sélectionnez ces champs puis saisissez *0* dans la zone de texte **« Freq »**. Juste après, appuyez sur **« SAVE »** et le défilement se désactivera, revenant aux valeurs par défaut.

Appuyez sur le bouton vert **« HOME »** en bas du tableau pour revenir à la page d'accueil.

### Préférences de charge & Journal {#sec:web_charging_prefs}

Cette page se divise en deux tableaux principaux : le premier sert à contrôler le processus de charge, tandis que le second contient la liste des 15 dernières charges accompagnées de données supplémentaires.

#### Préférences de charge

En commençant par les plus utiles, nous avons le champ **« Charging status »** qui contient les informations sur le statut actuel de la voiture, y compris le *secteur 220V* et le *processus de charge* avec leurs drapeaux ON et OFF.

Juste en dessous se trouve la case **« Charge power limit »**, où vous pouvez choisir la puissance que votre Twizy peut utiliser pendant la charge, allant de $0,4 kW$ jusqu'à $2,3 kW$ avec 7 niveaux au choix (sélectionnez *0 pour désactiver la limite de puissance*).

Dans le coin supérieur droit se trouve le bouton **« ABORT CHARGING »**, qui interrompt immédiatement et proprement le processus de charge, tout comme celui présent sur l'écran du ToM+ dans la page de réglages que nous avons abordée dans la Section [3.10](#sec:settings_page){reference-type="ref" reference="sec:settings_page"}.

<figure data-latex-placement="H">
<img src="figures/charging_process.png" style="width:100.0%" />
<figcaption>Page des préférences de charge — Tableau de contrôle du processus de charge.</figcaption>
</figure>

Juste après se trouve le champ **« Stop charge at SOC % »**, qui correspond au pourcentage de charge auquel ToM+ envoie automatiquement le signal d'interruption du processus de charge. Pour votre information, limiter la plage de charge maximale (95 % ou moins) ralentira la dégradation du SOH de la batterie.

En passant au champ suivant, nous avons le champ **« Full charge after »** qui est étroitement lié au précédent. En clair, cela n'arrêtera pas la charge au SOC sélectionné une fois toutes les *X* charges (*par exemple 10* comme sur l'image). Gardez à l'esprit qu'une charge à 100 % de temps en temps est utile pour rééquilibrer la tension des cellules de la batterie.

Un autre champ associé est l'option **« Max charge once (next/current) »**, qui fonctionne comme un bouton et ordonne à ToM+ d'effectuer une charge complète sans l'interruption au SOC choisi. Cela prévaut sur le champ précédent et s'appliquera, **après avoir appuyé sur « SAVE »**, au processus de charge en cours s'il a déjà commencé ou au suivant dans le cas contraire.\
Nous avons ensuite un champ de sécurité, **« Charger max temperature »**, dans lequel vous pouvez définir un seuil (valeur entière exprimée en °C). Si ce seuil est dépassé avec une marge d'hystérésis définie par l'utilisateur, ToM+ réduit progressivement le niveau de limite de puissance que nous avons vu auparavant. Il continue de la réduire, de deux niveaux si nécessaire, jusqu'à ce que la température redevienne normale, entraînant le retour à la normale de la limite de puissance.

La marge susmentionnée est personnalisable dans le champ approprié **« Temp margin »**, où vous pouvez saisir une valeur entière (exprimée en °C), qui sera ajoutée à la température maximale du chargeur pour assouplir le seuil avant de réduire la puissance de charge.

Un autre champ associé est **« Abort temperature »**, qui contient le dernier seuil de sécurité pour la température du chargeur. S'il est dépassé, ToM+ interrompt immédiatement la charge.\
Ensuite, nous avons trois champs de contrôle MQTT, distingués par leur numéro progressif. Cocher l'un de ces drapeaux vous permet de configurer à distance le paramètre situé à sa gauche via le protocole MQTT. Pour ce faire, après avoir activé le champ approprié et **appuyé sur « SAVE »**, il vous suffira de publier un message MQTT sur le topic spécifié entre parenthèses (ex. *001* ou *002*) sur votre broker (configuré dans la Section [4.2.4](#sec:mqtt_connection){reference-type="ref" reference="sec:mqtt_connection"}).

Si vous activez le **MQTT control (001)**, vous pouvez démarrer et arrêter la charge en publiant soit *0* soit *1* sur le topic MQTT *001*. Il en va de même pour le **MQTT control (002)** en publiant sur *002* une valeur comprise entre *0* et *7*, et le **MQTT control (003)** sur *003* avec une valeur comprise entre *0* et *100*.\
Enfin, nous trouvons le champ **« Aux Cmd »**, qui désigne la commande auxiliaire et se comporte comme celui que nous avons déjà abordé dans la page des déclencheurs d'alarme de la Section [4.4.8](#sec:web_alarm_triggers){reference-type="ref" reference="sec:web_alarm_triggers"}. Il est envoyé lorsque la charge est terminée ou lorsque la charge s'arrête au SOC spécifié.\
Après toute modification, appuyez sur le bouton **« SAVE »** pour *enregistrer vos changements*, sinon ils seront perdus lorsque vous quitterez la page.

#### Historique de charge

Le tableau de l'historique de charge conserve les quinze derniers processus de charge ainsi que des valeurs utiles pour les enrichir. Comme vous pouvez le constater, on y retrouve la date et l'heure, ainsi que la valeur des **kilomètres ODO** au début de la charge. À côté, nous avons la durée de la charge et la puissance moyenne **Average Power**, ainsi que les kWh rechargés **charged kWh**. Enfin, nous avons le *init SOC* et le *end SOC*, qui correspondent aux pourcentages de début et de fin de charge.\
La dernière colonne contient des **Notes** supplémentaires sur l'état de la charge, comme la façon dont elle s'est arrêtée (soit le SOC d'arrêt a été atteint, soit l'arrêt a été manuel) ou si elle est toujours en cours.

Si vous le souhaitez, vous pouvez également supprimer manuellement certains enregistrements en appuyant sur le bouton *X* à la fin de l'enregistrement concerné. Il est possible de tous les supprimer d'un coup en appuyant sur le bouton **« CLEAR HISTORY »** situé dans la partie inférieure du tableau.

<figure data-latex-placement="H">
<img src="figures/charging_history.png" style="width:95.0%" />
<figcaption>Page des préférences de charge — Tableau de l’historique de charge.</figcaption>
</figure>

Appuyez sur le bouton vert **« HOME »** sous le dernier tableau pour revenir à la page d'accueil.

### Page Heure & Date {#sec:web_time_date}

Avec votre ToM+, vous pouvez consulter la date et l'heure actuelles, mais comment les régler ? Cette page a été conçue exactement à cet effet et ne contient qu'un seul tableau présenté sur l'image ci-dessous.

<figure data-latex-placement="H">
<img src="figures/time_page.png" style="width:100.0%" />
<figcaption>Tableau de l’Heure &amp; Date actuelles.</figcaption>
</figure>

Les cinq premiers champs sont explicites et intuitifs, il suffit de régler la date et l'heure en fonction de votre fuseau horaire. La case à cocher **« DST »**, qui signifie Daylight Saving Time (Heure d'été), vous permet d'activer ou de désactiver le décalage d'une heure selon la saison.

Lorsque vous souhaitez confirmer vos modifications et les appliquer à ToM+, appuyez simplement sur le bouton **« SET »** et elles seront mises à jour.\
Ensuite, nous avons un champ très utile, l'option **« Synchronize clock with WiFi »**, pratique lorsque vous avez déjà configuré une connexion Wi-Fi comme expliqué dans la Section [4.1.2](#sec:add_wifi_profile){reference-type="ref" reference="sec:add_wifi_profile"}. Activez-la simplement et laissez ToM+ faire le travail.

Juste en dessous se trouve une valeur plus technique concernant la date et l'heure qui indique à ToM+ quel est votre fuseau horaire actuel (**TZ**) à l'aide d'une chaîne appelée **« POSIX »**. Cela inclut le moment où le décalage d'une heure de l'heure d'été est appliqué. Dans la plupart des pays d'Europe centrale, la chaîne est la suivante : *CET-1CEST,M3.5.0/2,M10.5.0/3*. Recherchez sur Internet la chaîne POSIX TZ de votre pays en cas de doute.\
Comme toujours, n'oubliez pas d'enregistrer vos modifications en appuyant sur le bouton **« SAVE »** au bas du tableau, sinon elles seront perdues quand vous quitterez la page.

Appuyez sur le bouton vert **« HOME »** sous le tableau pour revenir à la page d'accueil.

### Page des réglages BigToM / ToM+ {#sec:web_btom_tom_sets}

Sur cette page, vous pouvez personnaliser certains paramètres de votre BigToM ou ToM+, car cette page contient principalement des configurations pour la **page du tableau de bord**, disponible uniquement sur ces deux appareils.

<figure data-latex-placement="H">
<img src="figures/btom_page.png" style="width:100.0%" />
<figcaption>Tableau des réglages BigToM \ToM+.</figcaption>
</figure>

Lors du remplacement de votre tableau de bord par un BigToM, vous devrez peut-être ajouter ou soustraire des kilomètres à l'ODO du nouveau tableau de bord pour retrouver votre kilométrage d'origine. En effet, ils sont stockés dans la carte mère du tableau de bord. Ainsi, le premier paramètre est le champ **« ODO kms offset »**, utilisé pour corriger cette différence de kilomètres.

Comme vous le savez peut-être, les indicateurs de vitesse du tableau de bord sont délibérément majorés de $3 km/h$ pour des raisons de sécurité. Si vous souhaitez voir votre vitesse réelle, activez simplement l'option **« Real speed (not ODO) »** dans la deuxième ligne du tableau.\
Examinons maintenant l'option **« Lock touch while driving »**. Si elle est active, l'écran tactile sera désactivé pendant la conduite (c'est-à-dire vitesse $>0$) pour des raisons de sécurité.

Ensuite, nous avons l'option **Skip welcome animation**, qui peut être activée si vous êtes lassé de voir l'animation de bienvenue lors du passage du tableau de bord à une autre page.\
Il y a ensuite une section dédiée à la barre de puissance montrée sur la Figure [3.1](#fig:dashboard_layout){reference-type="ref" reference="fig:dashboard_layout"} en haut de la disposition du tableau de bord. Vous pouvez choisir ici, en utilisant la zone de choix **« Power bar item »**, quelle valeur doit être affichée et utilisée pour remplir la barre de puissance. Il y a trois données disponibles : *Engine Torque* (Couple moteur), *Battery Ampere* (Ampérage batterie) ou *Battery kW* (Kilowatts batterie).

Les deux champs **« Up/Down section scale % »** ci-dessous servent à ajuster la plage de la barre de puissance et représentent le pourcentage de la valeur maximale/minimale de l'élément de donnée sélectionné. Dans l'image d'exemple, pour la plage maximale, j'ai indiqué *30%*.\
Dans la section suivante, nous pouvons activer une autre fonctionnalité intéressante, présentée également sur la Figure [3.1](#fig:dashboard_layout){reference-type="ref" reference="fig:dashboard_layout"}, juste en dessous de l'indicateur de vitesse. Cela s'effectue en activant la case **« Enable alert speed bar »**, qui comporte trois seuils personnalisables, chacun correspondant à une couleur allant du *vert* au *jaune* puis au *rouge*.

Les trois champs suivants, **« Speed alert low/medium/high limit »**, sont destinés à être remplis avec les vitesses de seuil respectives en $km/h$ pour allumer la barre de vitesse avec la couleur appropriée. Dans l'exemple, la barre deviendra jaune en dépassant $50 km/h$ puis rouge en dépassant $70 km/h$. Comme vous pouvez le remarquer, je ne voulais pas que la barre verte s'affiche, j'ai donc réglé la valeur du seuil *low* sur la même valeur que le seuil *medium*.\
L'avant-dernière fonction est l'option **« 3D layout for charging page »**, activée par défaut, qui affiche des détails en 3D au lieu de la page de charge ToM standard.

Et enfin, la fonctionnalité la plus récemment ajoutée s'appelle le **Twin ToM**, conçue pour les propriétaires du ToM d'origine avant la sortie du ToM+. Cela vous permet d'utiliser le plus petit écran en combinaison avec la nouvelle version à clipser, afin de surveiller deux pages simultanément. Mais pour que cela fonctionne, vous devez activer l'option de la dernière ligne, **« Enable auxiliary display »**.

Vous pouvez ensuite sélectionner, avec la zone de choix **« Start page »**, une page spécifique à afficher sur l'écran auxiliaire lors de l'allumage, ou simplement choisir *Last shown* (Dernière affichée).\
Comme toujours, n'oubliez pas d'enregistrer vos modifications en appuyant sur le bouton **« SAVE »** en bas du tableau, sinon elles seront perdues lorsque vous quitterez la page.

Appuyez sur le bouton vert **« HOME »** sous le tableau pour revenir à la page d'accueil.

### Page de diagnostic {#sec:web_diagnostic}

Cette page se compose d'un seul tableau et vous permet de consulter plus d'informations sur les 10 dernières erreurs survenues sur votre Twizy, de manière similaire à la page d'affichage du ToM+ abordée dans la Section [3.8](#sec:error_page){reference-type="ref" reference="sec:error_page"}.

Les valeurs affichées sont le **« DTC Number »** et, si disponible, le **« DF Number »**, qui sont des identifiants uniques pour les erreurs de la Twizy, vous permettant de faire des recherches en ligne. Ensuite, nous avons le statut de l'erreur **« Status »**, tel que *SAVED* si elle s'est déjà produite ou *PRESENT* si elle vient tout juste de se produire.

Pour *activer les numéros DF*, veuillez vous référer à la Section [4.1.2](#sec:add_wifi_profile){reference-type="ref" reference="sec:add_wifi_profile"}.

<figure data-latex-placement="H">
<img src="figures/error_page.png" style="width:100.0%" />
<figcaption>Page de diagnostic — Tableau de la liste des erreurs.</figcaption>
</figure>

En plus de ces valeurs, les quatre valeurs suivantes sont les références d' **« ODO »**, de **« SOC »**, de **« speed »** et de **« 12V Battery voltage »** au moment où l'erreur correspondante s'est produite.

Pour chaque enregistrement d'erreur, s'il est disponible, il existe un champ de description d'erreur **« Description »**.\
Si vous souhaitez effacer les erreurs de la Twizy, y compris les erreurs fatales, vous pouvez appuyer sur le bouton **« DELETE ERRORS »** ci-dessous, qui les supprimera toutes en une seule fois.

Appuyez sur le bouton vert **« HOME »** situé sous le tableau pour revenir à la page d'accueil.

# Comment mettre à jour le firmware de votre ToM+ {#sec:update_procedure}

## Prérequis avant la mise à jour

ToM+ évolue constamment, car presque chaque jour je reçois des suggestions pour améliorer certaines fonctionnalités ou même en ajouter de très intéressantes. J'essaie de prendre en compte tous les conseils de chaque propriétaire, et ces conseils et idées se traduisent par des mises à jour du firmware. Lors des tests de l'appareil en conduite, si vous remarquez des bugs ou des comportements étranges, n'hésitez pas à me les signaler afin qu'ils fassent l'objet de correctifs. Comme je l'ai dit au début, ToM+ s'améliore continuellement, alors restez à l'écoute...

### Pourquoi devrais-je mettre à jour ?

Une nouvelle mise à jour apporte de nouvelles fonctionnalités et des corrections de bugs, alors pourquoi conserver une ancienne version du firmware quand vous pouvez facilement installer la dernière version stable ? Il n'y a donc aucune raison de garder votre ToM+ obsolète, puisque la mise à jour de son logiciel est **gratuite à vie** et vous procurera beaucoup de satisfaction et de plaisir en essayant les nouvelles fonctionnalités. En fin de compte, je vous conseille personnellement de maintenir votre ToM+ à jour pour plus de sécurité.\
Quoi qu'il en soit, toutes les anciennes versions du firmware restent disponibles sur le forum Twizy dans la section ToM (<https://www.twizy-forum.de/twiz-o-meter>) sous les sujets *"\[Twiz o'meter\] Update to firmware x.x"*. En fait, ToM+ permet également les retours à une version antérieure (downgrades) si nécessaire.

### De quoi ai-je besoin pour la mise à jour ?

Dans les sections suivantes, nous aborderons une méthode alternative de mise à jour, nettement plus chronophage par rapport à la méthode OTA déjà expliquée dans la Section [4.4.10](#sec:web_ota_update){reference-type="ref" reference="sec:web_ota_update"}. Je **recommande personnellement la méthode OTA**, car elle est plus sûre et plus facile à réaliser si vous n'êtes pas vraiment expert en informatique et systèmes embarqués.\
Si vous êtes toujours convaincu de vouloir mettre à jour le firmware de votre ToM+ avec la seconde méthode, il y a quelques éléments dont vous aurez besoin pour mener à bien la mise à jour. Tout d'abord, il vous faudra un ordinateur (un ordinateur de bureau ou un portable fera parfaitement l'affaire).

Plus tard, nous verrons comment connecter ToM+ à notre ordinateur afin de lui transférer les nouveaux fichiers de mise à jour. La deuxième chose à vous procurer est un câble micro-USB, le même que celui habituellement utilisé pour les appareils rechargeables et les anciens smartphones. Vous aurez également besoin d'une carte microSD d'une capacité de stockage comprise entre 8 et 32 Go. Des exemples sont présentés sur les photos ci-dessous. Et bien sûr, vous aurez besoin de votre ToM+ !

<figure data-latex-placement="H">
<img src="figures/cables_sd_update.png" style="width:80.0%" />
<figcaption>Câbles microUSB et exemple de carte microSD.</figcaption>
</figure>

### À quoi ressemblent les fichiers de mise à jour ? {#sec:update_files}

Avant de mettre à jour le firmware, vous devez évidemment télécharger depuis le forum Twizy (à nouveau <https://www.twizy-forum.de/twiz-o-meter>) le fichier ZIP de la version souhaitée. Vous devrez probablement vous inscrire sur le forum pour voir et télécharger les fichiers de firmware et les images. C'est une communauté très sympathique et active, je vous conseille donc de devenir membre quoi qu'il en soit. Après avoir extrait les fichiers dans le dossier, voici ce que vous devriez obtenir :

<figure data-latex-placement="H">
<img src="figures/firmware_release_folder.png" style="width:100.0%" />
<figcaption>Liste des fichiers du dossier de version du firmware.</figcaption>
</figure>

Tout d'abord, nous remarquons un fichier texte nommé *changeLog23.txt*, utilisé pour suivre les fonctionnalités ajoutées et les bugs corrigés dans la dernière version du firmware. Lisez-le si vous êtes curieux de savoir ce qui est nouveau ou si vous avez besoin d'aide supplémentaire pour la procédure de mise à jour.\
Ensuite, il y a deux dossiers contenant la mise à jour du **firmware de l'écran LCD** au format *.tft*. **Choisissez la version** conçue pour votre appareil : le premier dossier si vous possédez un ToM+ ou un BigToM (c'est-à-dire avec un plus grand écran), ou l'autre si vous avez un ToM traditionnel ou si vous souhaitez mettre à jour le Twin ToM (écran plus petit). C'est une étape cruciale, sinon les nouvelles icônes et graphismes ne s'adapteront pas à la taille de votre écran.\
Le dernier fichier est le fichier binaire *ESP32Fw23.bin* pour la **mise à jour du boîtier noir**. Assurez-vous de posséder tous ces fichiers, car vous en aurez besoin dans les étapes suivantes.

### Que dois-je savoir avant la mise à jour ?

Préparons maintenant notre ToM+ pour la mise à jour en **basculant l'interrupteur sur OFF** sur le boîtier noir. Assurez-vous de l'éteindre (*c'est-à-dire le symbole 0 sur l'interrupteur*), sinon vous causerez très certainement de graves problèmes au ToM+.

Ainsi, si votre Twizy est toujours sous tension avec la clé sur le contact, éteignez-la complètement et retirez la clé de contact. Après ces étapes simples, vous êtes prêt à commencer la procédure de mise à jour, mais veillez à suivre scrupuleusement les instructions de ce guide. Ne procédez pas par intuition, sous peine de risquer de bloquer définitivement (bricker) votre appareil.\
Le processus de mise à jour est assez simple et vous devrez mettre à jour à la fois le firmware de l'écran LCD et celui du boîtier noir, dans cet ordre précis. Nous verrons comment procéder dans la section suivante.

## Mise à jour du firmware de l'écran LCD

L'écran LCD est l'un des composants essentiels de ToM+, comme cela a été abordé dans les deux premiers chapitres, et pour cette raison, il doit également être mis à jour. Un nouveau firmware signifie de nouvelles icônes et des dispositions différentes, et pour pouvoir les charger sur l'écran, il est crucial d'utiliser une petite **carte microSD**. L'emplacement pour carte SD du ToM+ se trouve sous l'écran ; vous devrez donc peut-être le retirer temporairement de votre boîte à gants pour pouvoir y travailler plus facilement, ou simplement le basculer vers l'arrière et vous verrez l'ouverture.

### Préparation de la carte microSD

Malheureusement, toutes les cartes microSD ne fonctionnent pas avec l'écran, en particulier les plus récentes conçues pour les appareils photo, mais pour l'instant, j'ai testé des cartes Classe 10 HC de 8 à 32 Go et elles semblent bien fonctionner. N'hésitez pas à essayer avec votre propre carte mémoire pour voir si elle fonctionne.\
Maintenant que nous avons choisi une carte microSD, qui doit avoir une capacité de stockage **comprise entre 8 et 32 Go**, nous devons y copier le firmware LCD. Avant de copier le fichier sur la carte, nous devons nous assurer qu'il n'y a pas d'autres fichiers, sinon la mise à jour ne fonctionnera pas.

Déplacez donc tous vos fichiers vers votre ordinateur et formatez la carte microSD au **format FAT32** comme je l'ai fait sur la capture d'écran ci-contre. Pour ce faire, faites un clic droit sur l'icône de la carte dans votre explorateur de fichiers et sélectionnez l'option **"Formater"** dans le menu déroulant.

<figure data-latex-placement="H">
<img src="figures/forma_sd_steps.png" style="width:70.0%" />
<figcaption>Étapes pour formater la microSD en FAT32.</figcaption>
</figure>

Comme montré sur l'image, sélectionnez le système de fichiers **FAT32**, puis cochez l'option **"Formatage rapide"** et appuyez sur le bouton **"Démarrer"** pour lancer le processus. Patientez jusqu'à la fin, puis copiez le fichier *.tft* fourni dans la version du firmware que vous souhaitez installer, situé dans le dossier ZIP de mise à jour.

### Insertion de la carte microSD

Nous sommes maintenant prêts à insérer la carte microSD dans l'emplacement de l'écran LCD. Il peut être utile d'utiliser une pince à bec fin pour insérer délicatement la carte microSD. Cela vous permettra de bien centrer la carte dans l'emplacement interne.\
**RAPPEL !** La carte microSD ne s'insère dans l'emplacement que dans un seul sens, le côté des contacts orienté vers la surface de l'écran, comme montré sur l'image. Si elle ne rentre pas, ne forcez pas ! Essayez de la tourner de l'autre côté.

Maintenant que la carte microSD est insérée dans l'emplacement interne, poussez-la doucement dans le boîtier jusqu'à entendre un « clic ». Cela signifie que vous pouvez retirer la pince en toute sécurité sans risquer de perdre la carte à l'intérieur du boîtier.

<figure data-latex-placement="H">
<img src="figures/sd_insert.jpg" style="width:60.0%" />
<figcaption>Insérer la microSD dans l’ouverture de l’écran.</figcaption>
</figure>

### Déroulement de la mise à jour

Une fois la microSD insérée, nous pouvons poursuivre la procédure de mise à jour. Retournez à votre Twizy et rebranchez l'écran au boîtier noir. Ensuite, allumez l'écran à l'aide de l'interrupteur du boîtier noir (*c'est-à-dire le symbole 1 sur l'interrupteur*), et seulement après cela, mettez le contact de votre Twizy avec la clé.

Attendez que l'écran LCD lance le processus de mise à jour jusqu'à ce que vous voyiez le pourcentage de progression s'afficher, comme le montre la figure ci-dessous (pour l'écran du ToM+ comme du ToM). Le processus de copie depuis la microSD prend généralement jusqu'à une minute et demie.

<figure data-latex-placement="ht">
<figure>
<img src="figures/update_screen_lcd.jpg" />
<figcaption>Mise à jour de l’écran du ToM+.</figcaption>
</figure>
<figure>
<img src="figures/copy_sd_card.png" />
<figcaption>Mise à jour de l’écran du ToM.</figcaption>
</figure>
<figcaption>Mise à jour de l’écran du ToM.</figcaption>
</figure>

Une fois la mise à jour du firmware LCD terminée avec succès, cet écran s'affichera, indiquant **"Update Succeeded!"** (Mise à jour réussie !). Après la mise à jour, **NE PAS** rallumer l'appareil avec la carte microSD insérée ! Nous pouvons maintenant éteindre le véhicule et éteindre à nouveau ToM+ via l'interrupteur du boîtier noir.

Ensuite, retirez la carte microSD pendant que l'ensemble du système est hors tension ; la mise à jour de l'écran LCD est terminée. **RAPPEL !** Si vous retirez la carte alors que ToM+ est sous tension, vous bloquerez définitivement (bricker) l'appareil ! Après cela, sans modifier l'état général du système, passons à la mise à jour du boîtier noir, comme expliqué dans la section suivante.

## Mise à jour du firmware du boîtier noir (Windows)

Le boîtier noir est le deuxième composant essentiel du ToM+ et constitue le cerveau de tout le système. Si nous mettons à jour uniquement l'écran, le boîtier noir ne saura pas à quoi correspondent ces nouvelles icônes, ce qui entraînera des erreurs de communication.

Il est donc crucial d'installer également le nouveau firmware sur la carte mère du ToM+. Pour ce faire, nous n'aurons plus besoin de la carte microSD, mais nous utiliserons le câble microUSB préparé précédemment et l'ordinateur. En effet, nous allons flasher le firmware directement sur la carte ESP32 pour y installer le nouveau logiciel.

### Préparation de l'ordinateur

Avant de brancher le câble sur l'ordinateur, nous devons installer certains programmes pour qu'il fonctionne correctement. La **carte ESP32** nécessite des pilotes (drivers) pour être reconnue par le système d'exploitation ; nous allons donc les télécharger directement depuis le site officiel.

Depuis la page de téléchargement du [site Silicon Labs](https://www.silabs.com/software-and-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads), nous devons choisir la version correspondant à notre système d'exploitation, comme le montre la capture d'écran ci-dessous.

<figure data-latex-placement="H">
<img src="figures/driver_download.png" style="width:100.0%" />
<figcaption>Page de téléchargement des pilotes sur Silicon Labs.</figcaption>
</figure>

Cette section du guide étant spécifique au système d'exploitation Windows, nous allons télécharger le paquet *"CP210x Windows Drivers"* en cliquant sur le lien surligné en jaune sur l'image ci-dessus.

Le fichier téléchargé sera une archive ZIP, généralement nommée *"CP210xWindowsDrivers.zip"*, contenant quelques dossiers et plusieurs fichiers. La capture d'écran ci-dessous présente la liste habituelle des fichiers contenus dans l'archive ZIP.

<figure data-latex-placement="H">
<img src="figures/driver_folder.png" style="width:70.0%" />
<figcaption>Contenu de l’archive ZIP des pilotes.</figcaption>
</figure>

Extrayez tous les fichiers dans un dossier temporaire sur votre Bureau. Il est maintenant important de choisir le bon fichier *".exe"* à exécuter pour installer les pilotes. Si votre système d'exploitation est en 64 bits (ce qui est le cas de la plupart des ordinateurs), exécutez le fichier *CP210xVCPInstallerx64.exe* ; sinon, le second fichier *".exe"* sera celui adapté, comme le montre l'image.

Veillez à exécuter le fichier exécutable avec les privilèges d'administrateur en faisant un clic droit dessus et en sélectionnant l'option **"Exécuter en tant qu'administrateur"**. Si vous y êtes invité, autorisez le programme à effectuer des opérations d'administration sur votre ordinateur, faute de quoi le processus d'installation du pilote ne démarrera pas.

<figure data-latex-placement="ht">
<figure>
<img src="figures/wizard_step1.png" />
<figcaption>Première étape : Appuyez sur « Suivant ».</figcaption>
</figure>
<figure>
<img src="figures/wizard_step2.png" />
<figcaption>Deuxième étape : « Accepter » puis « Suivant ».</figcaption>
</figure>
<figcaption>Deuxième étape : « Accepter » puis « Suivant ».</figcaption>
</figure>

Une fois l'assistant d'installation lancé, une fenêtre semblable à celle de gauche s'affiche. Il s'agit d'un outil d'installation pas à pas pour les pilotes nécessaires à la reconnaissance du boîtier noir par votre ordinateur. Appuyez sur le bouton **"Suivant"** comme indiqué ici pour démarrer le processus.\
La fenêtre suivante qui devrait apparaître est celle présentée à droite. Ici, vous devez accepter la licence en cochant la première option **"Accepter la licence"**. Ensuite, vous pouvez cliquer sur le bouton **"Suivant"** comme indiqué et démarrer la copie des pilotes dans le bon dossier système : patientez jusqu'à la fin de la copie.

Une fois la copie terminée, l'installation des pilotes CP210X est achevée et vous pouvez brancher le boîtier noir à votre ordinateur en toute sécurité. Cliquez ensuite sur le bouton **"Terminer"** pour fermer la fenêtre.\
Avant de faire quoi que ce soit, assurez-vous que l'interrupteur du boîtier noir ToM+ est bien éteint (*c'est-à-dire le symbole 0 sur l'interrupteur*). La Twizy doit également être hors tension, car si vous branchez le câble sur votre PC alors que le ToM+ est encore alimenté par le véhicule, vous allez mélanger les alimentations (5V et 12V) et le ToM+ sera définitivement endommagé.

<figure id="fig:black_box_labels" data-latex-placement="H">
<img src="figures/black_box.jpg" style="width:60.0%" />
<figcaption>Les composants du boîtier noir.</figcaption>
</figure>

Le boîtier noir dispose d'un petit connecteur microUSB sur sa face arrière, comme vous pouvez le voir sur l'image ci-dessus. Connectez donc l'extrémité microUSB du câble au boîtier noir. Ensuite, connectez l'extrémité USB du câble à un port USB libre de votre ordinateur.

**RAPPEL !** Les deux extrémités du câble ne s'insèrent que dans un seul sens dans les prises correspondantes, ne forcez donc pas au risque d'endommager le port du ToM+ ou celui de votre ordinateur. Essayez de le tourner de l'autre côté et vérifiez si cela fonctionne ainsi.\
Désormais, l'ordinateur devrait reconnaître la carte ESP32 du boîtier noir si vous avez correctement installé les pilotes. Pour le vérifier, recherchez l'application **"Gestionnaire de périphériques"** sur votre PC et exécutez-la.

Une fenêtre similaire à celle de la figure ci-dessous devrait s'ouvrir. Recherchez la ligne **"Ports (COM et LPT)"** avec une icône de connecteur et double-cliquez dessus pour ouvrir la liste de tous vos périphériques série. Comme sur la capture d'écran, recherchez *"Silicon Labs CP210x to UART Bridge (COMx)"* puis notez le numéro du port COM, qui est **COM8** dans cet exemple. Ce numéro sera utile à l'étape suivante pour indiquer au PC où télécharger la nouvelle version du firmware. Poursuivons le processus...

<figure data-latex-placement="H">
<img src="figures/device_manager.png" style="width:80.0%" />
<figcaption>Gestionnaire de périphériques - Port série UART (COM8).</figcaption>
</figure>

Visitez le [site officiel d'ESP32](https://www.espressif.com/en/support/download/other-tools) pour télécharger un outil nécessaire pour flasher le firmware sur la carte du boîtier noir. Recherchez **"Flash Download Tools"** et cliquez sur le bouton comme indiqué sur l'image. Ensuite, recherchez dans la page les *"Flash Download Tools"* avec l'icône de disquette et cliquez dessus.

Un fichier ZIP nommé *"flashdownloadtoolx.x.x.zip"* sera téléchargé, où les symboles « x » seront remplacés par le nom de la version, qui est **V3.9.11** dans cet exemple. En ouvrant le dossier ZIP téléchargé, vous remarquerez qu'il contient un autre dossier. Extrayez-le sur votre Bureau ou à l'emplacement de votre choix, puis ouvrez-le. Les fichiers qu'il contient sont généralement ceux énumérés sur la capture d'écran ci-dessous.

<figure data-latex-placement="H">
<img src="figures/esptool_folder.png" style="width:70.0%" />
<figcaption>Contenu du dossier ZIP des Flash Tools.</figcaption>
</figure>

Sélectionnez *"flashdownloadtool.11.exe"* ou la version que vous avez téléchargée et exécutez-le avec les droits d'administrateur en faisant un clic droit sur le fichier et en choisissant l'option **"Exécuter en tant qu'administrateur"**. Si vous y êtes invité, autorisez l'exécutable à effectuer des opérations sur votre ordinateur.\
Une fois le programme lancé, une fenêtre de terminal s'ouvre, qui va lancer en quelques secondes l'interface utilisateur. Elle devrait ressembler à la première image présentée dans l'exemple ci-dessous. Vous devez modifier le champ **"ChipType"** pour choisir *"ESP32"*, comme indiqué dans la deuxième étape ci-dessous. Laissez le reste inchangé et appuyez sur le bouton **"OK"**.

<figure data-latex-placement="H">
<img src="figures/launching_flashtool.png" style="width:85.0%" />
<figcaption>Sélection de la carte mère ESP32 dans le menu de choix.</figcaption>
</figure>

### Déroulement de la mise à jour

Dès que vous appuyez sur le bouton **"OK"**, la fenêtre *"ESP32 DOWNLOAD TOOL"* s'ouvre. Extrayez maintenant le fichier binaire (extension *.bin*) fourni dans le fichier ZIP de publication du firmware ToM+, comme nous l'avons vu à la Section [5.1.3](#sec:update_files){reference-type="ref" reference="sec:update_files"}.

Ensuite, appuyez sur le bouton **"..."** visible sur la première image et sélectionnez le chemin d'accès du fichier *".bin"*. Une fois cette opération effectuée, appuyez sur le bouton **"Ouvrir"** : une ligne verte contenant le chemin que vous venez de valider apparaît sur la première ligne.

Poursuivez en **cochant la case** située à côté de la première ligne, désignant le firmware que vous souhaitez charger. Saisissez ensuite dans la zone de texte visible sur la deuxième image la séquence de caractères suivante : **0$\times$`<!-- -->`{=html}10000** (avec quatre zéros). Cela représente l'adresse mémoire initiale où seront stockés les fichiers du firmware.

Vient enfin la dernière étape de la configuration : sélectionnez le numéro de port COM dans la liste déroulante située dans le coin inférieur droit. Veillez à sélectionner le bon port COM, c'est-à-dire celui que nous avons précédemment noté depuis le **Gestionnaire de périphériques**.

<figure data-latex-placement="H">
<img src="figures/flashtool_page.png" style="width:100.0%" />
<figcaption>Étapes de configuration de l’outil ESP32 Download Tool.</figcaption>
</figure>

Lançons à présent la mise à jour en appuyant sur le bouton **"START"** comme indiqué sur la première image. Une barre de progression verte apparaît en bas de la fenêtre et l'ensemble du processus prend généralement deux minutes.

Une fois le transfert terminé, le message **"FINISH"** s'affiche dans le cadran vert dans le coin inférieur gauche, comme montré sur l'image. En guise de confirmation supplémentaire, la barre de progression sera complète : la mise à jour est désormais terminée.

<figure data-latex-placement="H">
<img src="figures/flashtool_page2.png" style="width:100.0%" />
<figcaption>Finalisation de la mise à jour dans ESP32 Download Tool.</figcaption>
</figure>

Fermez cette fenêtre, puis vous pouvez débrancher le câble en toute sécurité, côté PC et côté ToM+. Ce n'est qu'après ces actions que vous pourrez rétablir l'alimentation normale du ToM+, en basculant l'interrupteur sur la position 1 et en mettant le contact de votre Twizy avec la clé.

Pour restaurer vos configurations précédentes, accédez à la page des paramètres du ToM+ en appuyant sur les trois points dans le coin supérieur droit, puis appuyez sur le bouton de sortie sans rien modifier. De cette façon, vous mettrez à jour la structure des données enregistrées dans la mémoire du boîtier noir et vos configurations seront à nouveau opérationnelles.\
**Félicitations !** Vous avez terminé l'ensemble de la procédure de mise à jour. Profitez bien du nouveau firmware, et n'oubliez pas de me signaler tout bug ou problème par message privé, idéalement en joignant une photo.

## Mise à jour du boîtier noir (Unix)

Le boîtier noir est le deuxième composant essentiel du ToM+ et constitue le cerveau de tout le système. Si nous mettons à jour uniquement l'écran, le boîtier noir ne saura pas à quoi correspondent ces nouvelles icônes, ce qui entraînera des erreurs de communication.

Il est donc crucial d'installer également le nouveau firmware sur la carte mère du ToM+. Pour ce faire, nous n'aurons plus besoin de la carte microSD, mais nous utiliserons le câble microUSB préparé précédemment et l'ordinateur. En effet, nous allons flasher le firmware directement sur la carte ESP32 pour y installer le nouveau logiciel.

Avant toute chose, basculez l'interrupteur du boîtier noir ToM+ sur OFF (*c'est-à-dire le symbole 0 sur l'interrupteur*) et éteignez également votre Twizy. C'est une étape importante à suivre scrupuleusement pour éviter d'endommager l'appareil.

### Préparation de l'ordinateur

Téléchargez le dossier de mise à jour du firmware ToM+ joint au message de publication du firmware. Extrayez maintenant le fichier binaire (extension *.bin*) contenu dans le ZIP de la release du firmware ToM+, comme nous l'avons expliqué à la Section [5.1.3](#sec:update_files){reference-type="ref" reference="sec:update_files"}. Le fichier s'appelle généralement *"FwXXESP32.bin"*, où les symboles *"XX"* seront remplacés par le numéro de version, par exemple *"23"*.\
**Avertissement :** *cette procédure pour le boîtier noir a été testée sous Ubuntu 20.04 (en espérant qu'elle fonctionne également sur d'autres distributions Unix). Ne branchez pas le boîtier noir tant que cela ne vous est pas explicitement demandé*.\
Nous devons maintenant installer le paquet esptool pour flasher le nouveau firmware sur le boîtier noir. Effectuez cette opération soit via l'interface du gestionnaire de paquets de votre distribution Unix, soit à l'aide de la commande appropriée dans un terminal. Par exemple, *"sudo apt-get esptool"*, comme le montre l'image. Si vous y êtes invité, saisissez le mot de passe de l'utilisateur sudo, puis appuyez sur ENTREE et patientez.

<figure data-latex-placement="H">
<img src="figures/apt_get_esptool.png" style="width:100.0%" />
<figcaption>Installation du paquet esptool sous Ubuntu.</figcaption>
</figure>

Ensuite, vous devez installer Python si vous ne l'avez pas déjà, car l'outil esptool est écrit en langage Python. Vous devez donc taper la commande *"sudo apt-get python"*, comme le montre l'image. À nouveau, si vous y êtes invité, saisissez le mot de passe de l'utilisateur sudo, appuyez sur ENTREE et patientez.

<figure data-latex-placement="H">
<img src="figures/apt_get_python.png" style="width:100.0%" />
<figcaption>Installation du paquet python sous Ubuntu.</figcaption>
</figure>

Une fois les deux paquets installés, tapez *"sudo tail -f /var/log/messages"* dans le terminal comme indiqué sur l'image pour surveiller en temps réel le fichier journal (log) qui nous indiquera à quel port COM le boîtier noir sera associé par le système d'exploitation. Si vous y êtes invité, saisissez le mot de passe de l'utilisateur sudo, puis appuyez sur ENTREE. **Nous pouvons maintenant brancher le boîtier noir**.

<figure data-latex-placement="H">
<img src="figures/tail_com.png" style="width:100.0%" />
<figcaption>Surveillance en temps réel des connexions COM.</figcaption>
</figure>

Le boîtier noir possède un petit connecteur microUSB sur sa face arrière, comme vous pouvez le voir sur la Figure [5.1](#fig:black_box_labels){reference-type="ref" reference="fig:black_box_labels"}. Connectez donc l'extrémité du câble microUSB au boîtier noir. Ensuite, connectez l'extrémité USB du câble à un port USB libre de votre ordinateur.

**RAPPEL !** Les deux côtés du câble ne s'insèrent que dans un seul sens dans leurs prises respectives, ne forcez donc pas au risque de casser le port du ToM+ ou celui de votre ordinateur. Essayez de le tourner de l'autre côté et vérifiez si cela fonctionne ainsi.\
Dès que vous branchez le boîtier noir à l'ordinateur, vous devriez obtenir une sortie similaire à celle présentée dans le bloc de code ci-dessous.

``` {.bash language="bash"}
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.232228] usb 1-3: new full-speed USB
device number 3 using xhci_hcd
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.423441] usb 1-3: New USB device found,
idVendor=10c4, idProduct=ea60, bcdDevice= 1.00
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.423453] usb 1-3: New USB device
strings: Mfr=1, Product=2, SerialNumber=3
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.423457] usb 1-3: Product: CP2102 USB
to UART Bridge Controller
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.423461] usb 1-3: Manufacturer: Silicon
Labs
85
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.423464] usb 1-3: SerialNumber: 0001
Oct 15 11:05:14 Kubuntu2004 mtp-probe: checking bus 1, device 3:
"/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-3"
Oct 15 11:05:14 Kubuntu2004 mtp-probe: bus: 1, device: 3 was not an MTP device
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.457397] usbcore: registered new
interface driver usbserial_generic
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.457415] usbserial: USB Serial support
registered for generic
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.460166] usbcore: registered new
interface driver cp210x
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.460185] usbserial: USB Serial support
registered for cp210x
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.460236] cp210x 1-3:1.0: cp210x
converter detected
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.464538] usb 1-3: cp210x converter now
attached to ttyUSB0
Oct 15 11:05:14 Kubuntu2004 mtp-probe: checking bus 1, device 3:
"/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-3"
Oct 15 11:05:14 Kubuntu2004 mtp-probe: bus: 1, device: 3 was not an MTP device
```

La ligne qui nous intéresse particulièrement est la suivante : *"cp210x converter now attached to ttyUSB0"* où le terme **"ttyUSB0"** correspond au port série auquel le boîtier noir est connecté. Notez ce nom de port (qui peut différer du mien), car nous en aurez besoin pour téléverser le nouveau firmware.

### Déroulement de la mise à jour

Naviguez avec votre gestionnaire de fichiers dans le dossier où se trouve le fichier *.bin* du firmware, puis ouvrez un terminal à cet endroit en faisant un clic droit sur le dossier et en choisissant l'option **"Ouvrir dans un terminal"** dans le menu déroulant. Si vous préférez, vous pouvez naviguer manuellement à travers vos dossiers à l'aide de la commande « cd » jusqu'à trouver le bon répertoire.

Une fois dans le bon dossier, exécutez cette commande longue et un peu fastidieuse, en remplaçant *"ttyUSBx"* par le nom du port série noté précédemment (ex. *"ttyUSB0"*) et *"ESP32FwXX.bin"* par le nom du fichier *".bin"* qui contient la version du firmware à charger sur le ToM+ (ex. *"ESP32Fw23.bin"*).

        python /usr/share/esptool/esptool.py --chip auto --port /dev/ttyUSBx --baud
    921600 --before default_reset --after hard_reset write_flash -z --flash_mode dio
    --flash_freq 40m --flash_size 4MB 0x10000 ESP32_FwXX.bin

Vous devriez obtenir une sortie similaire à la suivante :

``` {.bash language="bash"}
Serial port /dev/ttyUSB0
Connecting........_____.....____
Detecting chip type... ESP32
Chip is ESP32D0WDQ5 (revision 3)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme
None
Crystal is 40MHz
MAC: xx:xx:xx:xx:xx:xx
Changing baud rate to 921600
Changed.
Enabling default SPI flash mode...
Configuring flash size...
Erasing flash...
Compressed 716176 bytes to 461048...
Took 2.90s to erase flash block
Wrote 716176 bytes (461048 compressed) at 0x00010000 in 9.1 seconds (effective
630.3 kbit/s)...
Hash of data verified.
Leaving...
Hard resetting via RTS pin...
```

Fermez cette fenêtre ainsi que toutes les autres, puis débranchez le câble en toute sécurité du PC et du ToM+. Ce n'est qu'après ces actions que vous pourrez rétablir l'alimentation normale du ToM+, en basculant l'interrupteur sur la position 1 et en mettant le contact de votre Twizy avec la clé.

Pour restaurer vos configurations précédentes, accédez à la page des paramètres du ToM+ en appuyant sur les trois points dans le coin supérieur droit, puis appuyez sur le bouton de sortie sans rien modifier. De cette façon, vous mettrez à jour la structure des données enregistrées dans la mémoire du boîtier noir et vos configurations seront à nouveau opérationnelles.\
**Félicitations !** Vous avez terminé l'ensemble de la procédure de mise à jour. Profitez bien du nouveau firmware, et n'oubliez pas de me signaler tout bug ou problème par message privé, idéalement en joignant une photo.

# Réglage sur votre ToM+ (Twizy-cfg) {#apx:tuning}

## Qu'est-ce que Twizy-cfg ?

[Twizy-Cfg](http://github.com/dexterbg/Twizy-Cfg) est un shell de configuration **open-source** et léger conçu pour le contrôleur de moteur SEVCON Gen4 intégré dans la Renault Twizy, développé par [dexterbg](https://github.com/dexterbg). Développé pour fonctionner sur des microcontrôleurs Arduino équipés d'un module CAN-bus SPI MCP2515, cet outil fournit aux hackers matériels, techniciens et passionnés de VE une interface en ligne de commande directe pour interagir avec le système de transmission du véhicule via le port de **diagnostic OBD-II** standard.\
À son cœur, Twizy-Cfg agit comme un pont entre des commandes macro de *haut niveau* et des opérations de registre SDO (Service Data Object) CANopen de *bas niveau*. Il permet un réglage et une surveillance précis du groupe motopropulseur, offrant des fonctionnalités telles que :\

- Personnalisation du profil de conduite : Ajustement des paramètres clés de performance, notamment la puissance maximale, les limites de couple, la vitesse maximale et les rampes d'accélération.

- Gestion de l'énergie : Réglage fin des niveaux de récupération d'énergie pendant la roue libre et le freinage pour équilibrer l'autonomie de conduite et la force de freinage.

- Gestion des profils : Sauvegarde, chargement et restauration de profils de performance personnalisés directement depuis et vers l'EEPROM de l'Arduino.

- Diagnostics et accès bas niveau : Émission de commandes CANopen brutes et de requêtes de diagnostic OBD-II de base pour inspecter les états du contrôleur et les révisions du micrologiciel.

 \
Cet appendice couvrira la façon dont ToM+ peut gérer une partition spéciale avec le logiciel mentionné ci-dessus, adapté pour fonctionner sur sa carte ESP32 (puce ToM+).

## Prérequis avant de commencer

**AVERTISSEMENT !** L'objectif de cet appendice est d'installer et de faire fonctionner dans la boîte noire un micrologiciel alternatif, non codé par moi, en utilisant le matériel pour un usage différent de celui pour lequel il a été conçu. En suivant ce guide, vous aurez une **boîte noire à double démarrage**, avec le micrologiciel ToM+ et le micrologiciel Twizy-cfg coexistant, chacun amorçable selon vos besoins.\
Pour atteindre cet objectif, vous aurez besoin d'une boîte noire exécutant une version de micrologiciel **1.45** ou supérieure. Il s'agit d'une exigence cruciale, car ce processus nécessite la fonctionnalité de mise à jour OTA, introduite dans la version mentionnée. Consultez la Section [3.10](#sec:settings_page){reference-type="ref" reference="sec:settings_page"} pour vérifier la version du micrologiciel de votre ESP et la Section [4.4.10](#sec:web_ota_update){reference-type="ref" reference="sec:web_ota_update"} pour mettre à jour votre micrologiciel via OTA si nécessaire.\
Ensuite, vous aurez besoin de la version compilée de Twizy-cfg compatible ESP32, que vous pouvez télécharger depuis [ce lien](https://www.mediafire.com/file/n5waunl2w19cpl6/TwizyCfg_ok.ino.bin.zip/file). Extrayez son contenu et conservez le fichier *".bin"* dont nous aurons besoin plus tard.

## Le flux de travail de mise à jour

Connectez-vous maintenant au serveur web en suivant l'une des méthodes expliquées à la Section [4.4.2](#sec:web_server_access){reference-type="ref" reference="sec:web_server_access"}, puis naviguez vers la page **"OTA Update and Prefs"** (Section [4.4.10](#sec:web_ota_update){reference-type="ref" reference="sec:web_ota_update"}) et utilisez le fichier *".bin"* précédemment extrait pour effectuer la mise à jour, en cochant la case **"Update to special partition"** (sinon vous remplacerez le micrologiciel ToM+ d'origine).\

<figure data-latex-placement="H">
<img src="figures/ota_page3.png" style="width:100.0%" />
<figcaption>Page de mise à jour OTA — Table de mise à jour et d’informations.</figcaption>
</figure>

Lorsque la barre de progression de la mise à jour atteint 100%, l'écran LCD du ToM+ devient noir et c'est le signe concluant que ToM+ redémarre, en chargeant le logiciel *Twizy-cfg*. Maintenant, vous devez vous connecter au point d'accès **"Twizy-cfg"** sur votre appareil pour accéder à son serveur web et, si cela vous est demandé, accepter de maintenir la connexion active même si elle ne fournit pas d'accès Internet.

Le **mot de passe** est le mot de passe ToM+ par défaut, c'est-à-dire le mot "pass" suivi du numéro de série de votre appareil (par ex. *pass129777*). Le numéro de série se trouve sur la page des paramètres comme expliqué à la Figure [3.3](#fig:settings_page){reference-type="ref" reference="fig:settings_page"}.\
Maintenant, ouvrez un navigateur web et tapez **192.168.4.1/webserial** pour naviguer vers l'interface du serveur web, où vous pouvez envoyer des commandes de réglage. Le terminal de commande ressemble à celui montré sur l'image ici. Comme déjà dit, le réglage n'est pas une fonctionnalité officielle de ToM+ et *Twizy-cfg* n'a pas été écrit par moi, veuillez donc vous référer au [sujet Twizy-cfg](https://www.twizy-forum.de/projekte-twizy/83451-twizy-cfg-sevcon-shell-fuer-arduino?start=0) ou à son [dépôt Github](https://github.com/dexterbg/Twizy-Cfg) pour connaître les commandes et configurations de réglage.\

<figure data-latex-placement="H">
<img src="figures/TuningMonitor.PNG" style="width:70.0%" />
<figcaption>Moniteur de réglage pour exécuter les commandes de configuration.</figcaption>
</figure>

Tant que vous utilisez Twizy-cfg, le micrologiciel ToM+ ne sera pas chargé et l'écran ne s'allumera donc pas. Lorsque vous souhaitez revenir au micrologiciel officiel ToM+, il vous suffira de taper dans le moniteur de réglage cette commande explicite : **reboot**.\
Et voilà, ToM+ redémarre sur l'autre partition et revient à son comportement normal, et la configuration de réglage persistera dans votre Twizy. La prochaine fois que vous aurez besoin du shell Twizy-cfg, allez simplement sur la page **"OTA Update and Prefs"** du serveur web ToM+ et sélectionnez l'option *"REBOOT FROM SPECIAL PARTITION"* dans le tableau présenté dans l'image suivante. Pas besoin de téléverser à nouveau le fichier *".bin"*.

<figure data-latex-placement="H">
<img src="figures/ota_boot.png" style="width:100.0%" />
<figcaption>Page de mise à jour OTA — Tableau des options de démarrage.</figcaption>
</figure>

# Contrôle de l'interrupteur WiFi Tasmota {#apx:tasmota}

## Que sont les interrupteurs/prises WiFi ?

Dans cet appendice, j'expliquerai comment vous pouvez configurer votre ToM+ pour interagir avec un interrupteur AC WiFi / une prise AC, ou tout autre appareil exécutant un **micrologiciel Tasmota**.

Il s'agit essentiellement de *modules relais* qui peuvent être contrôlés à distance via une connexion sans fil. Vous pouvez facilement trouver ce genre d'appareils sur de nombreux sites d'e-commerce (comme Amazon), pour quelques dizaines d'euros.\
Ils existent sous plusieurs formats, mais ils apparaissent fréquemment sous les deux formes montrées dans l'image. La seconde est plus compacte et conviviale, tandis que la première nécessite des connexions par câble pour fonctionner avec vos équipements électriques.

<figure data-latex-placement="ht">
<figure>
<img src="figures/Sonoff.PNG" />
<figcaption>Interrupteur intelligent WiFi Sonoff.</figcaption>
</figure>
<figure>
<img src="figures/TasmotaPlug.PNG" />
<figcaption>Prise intelligente WiFi Tasmota.</figcaption>
</figure>
<figcaption>Prise intelligente WiFi Tasmota.</figcaption>
</figure>

*Mais pourquoi est-ce utile ?* Il existe de nombreuses raisons pour lesquelles vous pourriez avoir besoin de connecter ToM+ à ces appareils. Par exemple : vous souhaitez arrêter la charge de la batterie de traction si le chargeur surchauffe et reprendre la charge lorsque la température diminue ; ou peut-être souhaitez-vous **arrêter la charge** lorsqu'un SOC souhaité est atteint.

Ou encore, comme je l'ai fait dans cet appendice à des fins expérimentales, pour allumer une lampe dans ma chambre lorsque la Twizy (garée dans le garage) a presque terminé sa charge. En résumé, il existe de nombreuses idées utiles où un interrupteur/prise WiFi combiné à ToM+ peut aider à créer de superbes projets.

## Prérequis avant de commencer

Pour atteindre cet objectif, vous aurez besoin d'une boîte noire exécutant une version de micrologiciel **1.4** ou supérieure. Il s'agit d'une exigence cruciale, car ce processus nécessite des fonctionnalités introduites dans la version mentionnée. Consultez la Section [3.10](#sec:settings_page){reference-type="ref" reference="sec:settings_page"} pour vérifier la version du micrologiciel de votre ESP et la Section [4.4.10](#sec:web_ota_update){reference-type="ref" reference="sec:web_ota_update"} pour mettre à jour votre micrologiciel via OTA si nécessaire.

De plus, vous devrez avoir **configuré le WiFi et MQTT** pour faire fonctionner l'ensemble du système. Si ce n'est pas le cas, veuillez vous référer à la Section [4.1](#sec:wifi_settings){reference-type="ref" reference="sec:wifi_settings"} pour configurer le WiFi et à la Section [4.2.4](#sec:mqtt_connection){reference-type="ref" reference="sec:mqtt_connection"} pour la configuration MQTT. Ils doivent tous deux être activés et connectés pour accomplir cette tâche.\
Ensuite, vous aurez évidemment besoin d'un interrupteur ou d'une prise sans fil, selon vos besoins, et il doit exécuter un **micrologiciel Tasmota** (*version 7* ou supérieure).

Gardez à l'esprit que les appareils de type *"Sonoff"* sortent d'usine avec un micrologiciel propriétaire qui ne prend pas en charge nativement le protocole MQTT.\
Afin de les utiliser, comme je l'ai fait dans cet appendice, vous devez les mettre à niveau vers le micrologiciel Tasmota. Le web regorge de guides sur l'installation du micrologiciel Tasmota, recherchez donc celui qui convient à votre appareil et suivez-le. Pour les utilisateurs qui ne souhaitent pas effectuer la procédure de mise à jour du micrologiciel, je suggère personnellement d'acheter un appareil fonctionnant déjà sous le micrologiciel Tasmota.

## Configuration MQTT de Tasmota

Naviguez vers l'interface **Tasmota WebUI** et vous obtiendrez une page d'accueil similaire à celle présentée ci-dessous. À tout moment, en cas de doute, veuillez consulter la [documentation officielle](https://tasmota.github.io/docs/).

<figure data-latex-placement="H">
<img src="figures/Mqtt1.PNG" style="width:45.0%" />
<figcaption>Tasmota webUI — Page d’accueil.</figcaption>
</figure>

Tout d'abord, appuyez sur le bouton **"Configuration"** qui vous mènera à la page montrée dans la première image ci-dessous. Ensuite, configurez la *connexion WiFi*, en entrant vos paramètres (SSID et mot de passe) dans la page **"Configure WiFi"** de Tasmota. Ensuite, suivez les instructions pour configurer les *paramètres MQTT*, en accédant à la page webUI **"Configure MQTT"**.\

<figure data-latex-placement="ht">
<figure>
<img src="figures/Mqtt2.PNG" />
<figcaption>Page de configuration.</figcaption>
</figure>
<figure>
<img src="figures/Mqtt4.PNG" />
<figcaption>Page de configuration MQTT.</figcaption>
</figure>
<figcaption>Page de configuration MQTT.</figcaption>
</figure>

Entrez maintenant l'adresse de votre broker, votre ID utilisateur, votre mot de passe et le numéro de port. Ils doivent être les mêmes que ceux définis sur ToM+ ! Vous pouvez consulter l'explication de chaque champ dans la Section [4.2.4](#sec:mqtt_connection){reference-type="ref" reference="sec:mqtt_connection"}.\
Les paramètres les plus difficiles à comprendre sont **"Topic"** et **"Full Topic"**. Ceux-ci ne doivent pas être identiques aux topics MQTT de ToM+, car ils sont spécifiques à l'appareil que vous utilisez. Si vous mettez les mêmes topics *TOMin* et *TOMout*, les communications risquent de se perturber mutuellement.\
Dans le premier champ, entrez ce que vous voulez. Je suggère quelque chose qui rappelle la fonction de votre appareil. Mais veuillez utiliser une chaîne courte (5/6 caractères suffisent), car ce champ sera une partie minimale de la chaîne du topic complet et ToM+ a une limite de 50 caractères pour le champ **"Auxilliary MQTT command"** (discuté dans la Section [4.4.8](#sec:web_alarm_triggers){reference-type="ref" reference="sec:web_alarm_triggers"}).

Dans le second champ, il est important de distinguer deux options, selon le broker que vous utilisez. Si vous avez votre propre broker (c'est-à-dire *pas Maqiatto*), laissez la chaîne par défaut **%prefix%/%topic%/**.\
Si vous utilisez plutôt Maqiatto, configuré selon la Section [4.2.3](#sec:free_broker){reference-type="ref" reference="sec:free_broker"} ou tout autre broker qui ajoute *votre e-mail comme préfixe* du nom de topic, alors modifiez le champ **"Full Topic"** en conséquence. Les champs seront ceux présentés dans la deuxième image ci-dessus, ce qui donne **myemail@gmail.com/%prefix%/%topic%/**, en ajoutant votre userID (e-mail) comme préfixe.

Enfin, appuyez sur le bouton vert **"Save"** et attendez que l'appareil redémarre.\
**RAPPEL !** Si vous utilisez le broker Maqiatto, vous devrez peut-être ajouter le nouveau topic à votre compte comme expliqué à la Figure [4.2](#sec:free_broker_add_topics){reference-type="ref" reference="sec:free_broker_add_topics"}.

Dans ce cas, vous devrez ajouter **cmnd/\<votre nom de topic Tasmota\>/Power** comme nouveau nom de topic, qui deviendra *cmnd/charge/Power* si vous avez suivi l'image.

## Configuration Tasmota sur ToM+

Ouvrez le serveur web ToM+ comme expliqué dans la Section [4.4.2](#sec:web_server_access){reference-type="ref" reference="sec:web_server_access"} et allez sur la page **"Alarm triggers"**. Maintenant, ajoutez une nouvelle alarme à la liste en fonction de l'élément qui contrôlera votre appareil Tasmota, comme expliqué dans la Section [4.4.8](#sec:web_alarm_triggers){reference-type="ref" reference="sec:web_alarm_triggers"}.

Dans mon cas, j'ai choisi l'élément **"Battery SOC"**, qui déclenchera l'alarme lorsque sa valeur sera *égale à 97%*, pour notifier que la charge est presque terminée.

<figure data-latex-placement="H">
<img src="figures/Tom01.PNG" style="width:70.0%" />
<figcaption>Ajout du déclencheur Tasmota sur ToM+.</figcaption>
</figure>

Comme vous pouvez le remarquer, la partie la plus importante est de configurer correctement le champ **"Aux Cmd"**, car il contient la commande MQTT de contrôle que ToM+ enverra à l'appareil Tasmota.

Si vous avez votre propre broker MQTT (c'est-à-dire *pas Maqiatto*), la **Aux Cmd** aura cette syntaxe :

- *cmnd/\<votre nom de topic Tasmota\>/Power 1* si vous souhaitez allumer l'appareil.

- *cmnd/\<votre nom de topic Tasmota\>/Power 0* si vous souhaitez l'éteindre.

À nouveau, dans notre exemple, la commande devient **cmnd/charge/Power 1** pour allumer la lampe.\
Sinon, si vous utilisez le broker Maqiatto ou un autre qui utilise votre userID (e-mail) comme préfixe dans le nom des topics, la syntaxe de la **Aux Cmd** ressemblera à ceci :

- *myemail@gmail.com/cmnd/\<votre nom de topic Tasmota\>/Power 1* pour l'allumer.

- *myemail@gmail.com/cmnd/\<votre nom de topic Tasmota\>/Power 0* pour l'éteindre.

Dans notre cas, la commande devient **myemail@gmail.com/cmnd/charge/Power 1**.\
Si vous souhaitez arrêter la charge puis la redémarrer lorsque des conditions spécifiques sont remplies, vous devez ajouter deux alarmes, une pour chaque condition d'allumage/extinction (Power ON/OFF), en utilisant la syntaxe expliquée en conséquence.\
Veuillez noter que si vous avez un appareil avec plusieurs relais, vous devrez modifier la syntaxe ci-dessus en spécifiant quel relais vous souhaitez contrôler : en utilisant **"Power1"** pour le premier relais, **"Power2"** pour le second et ainsi de suite. Cela devient :

- *cmnd/\<votre nom de topic Tasmota\>/Power1 1* pour allumer le premier relais.

- *cmnd/\<votre nom de topic Tasmota\>/Power1 0* pour l'éteindre.

La même distinction de syntaxe concernant Maqiatto et les brokers possédés s'applique également ici.

## Problèmes courants et solutions

Certains micrologiciels Tasmota n'aiment pas le format de topic *Maqiatto*, donc si vous souhaitez piloter un appareil Tasmota avec ToM+, vous devez utiliser un autre broker MQTT. Après quelques tests, j'ai remarqué que vous pouvez utiliser avec succès [mqtt.dealgate.ru](https://dealgate.ru/), gratuit et plus riche en fonctionnalités.

L'inconvénient est que vous devez faire face à quelques traductions en russe pour créer le compte. Mais rien qu'un traducteur en ligne ne puisse résoudre.
