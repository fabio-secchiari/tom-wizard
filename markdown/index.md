::: titlepage
**TOM+ User Manual**

Version 2.0

![image](figures/tom_plus.png){width="85%" height="70%"}

Fabio Java

2026
:::

# Preface {#preface .unnumbered}

*This is ToM+ official user manual hand-written by me (Fabio Java) in English, without using any AI tool, neither in this guide nor in the code that makes ToM+ work. Other languages other than English have been automatically translated using* [DeepL](https://www.deepl.com/en/translator).\
*In an era of automated content generation, this manual stands apart and you can be confident that all provided features and user interface are human-written. This is what makes this project unique among any alternatives: knowing exactly what the code does is the key to consciously develop new features, fix bugs and guarantee support to other ToM+ owners if needed.*\
*ToM+ is costantly evolving with the help of its large community born out from the* [German Twizy forum](https://www.twizy-forum.de/twiz-o-meter). *If you would like to have a ToM+ unit, email me at* **info.twizometer@gmail.com**. *If you would like to suggest a new feature, report a bug or even a typo in this manual, please email me or open a pull request on* [Codeberg](https://codeberg.org/fabio-java/ToM-Wizard).\
*If you own a standard ToM or a BigToM, you can refer to this user manual as well, since the features are basically the same, except for standard ToM where the dashboard page and 3D charging pages are missing.*\
*This user manual is updated to 2.4 ESP firmware version.*

# Description and Features List

## ToM+ Feature Highlights

ToM+ has many functions and can be constantly updated along with the firmware development. In the next few paragraphs I will give you a brief introduction of its features, to give you an idea of the type of product that I will explain later in the manual.

### A new Twizy dashboard

Since the dashboard of our Twizy includes some values only, like the speed and the remaining kilometers, I decided to develop this cool display, that will show much more data, reading them directly from the Twizy CAN bus, using the OBD connector in the left glove box. ToM will just "sniff" the values sent out by the Twizy and then show them on the LCD display, allowing many other features. ToM has a tiny but powerful memory that is able to store some of these values while driving to give you a trip history. The capability of it to store some values, makes it possible to save your configurations and customizations on ToM, even after a firmware update.

<figure data-latex-placement="H">
<img src="figures/dashboard.jpg" style="width:80.0%" />
<figcaption>Dashboard of the ToM+</figcaption>
</figure>

It tries to keep the same style of the original Twizy dashboard, but with a more modern and 3D look. As the original one you have the battery, gear, the remaining kilometers, the speed and the time. But I added the exact **battery percentage**, the engine torque, some status icons, trip information and a lot of other stuff that you can configure as you wish and we will see in detail later.

The main page is customizable and you can choose what to show on it, as well as the other pages that you can scroll through using the button you can mount on the wiper stalk. The general look of the other pages is shown in the image, with one value in the foreground and the others in the left side. In the bottom you can change the shown page by tapping its icon.

<figure data-latex-placement="H">
<img src="figures/engine_page.jpg" style="width:80.0%" />
<figcaption>Engine page of the ToM+</figcaption>
</figure>

### WiFi connectivity

The ESP32 board contained in the black box have the capability to connect to a WiFi network access point. Once ToM+ is connected you can do plenty of things. For instance, this device can be used to transfer data from your Twizy to your personal **MQTT** broker, where you can use these values to embed your car in your home automation IoT system.

This is not the only feature related to the Wi-Fi capability that ToM+ has. It's able to be an access point as well with its SSID and password, creating a private network with no Internet connection. In this way you can safely connect, **accepting to keep the connection** profile active even if it doesn't provide any Internet connection (it usually appears with a notify in Android phones 10 seconds after the first connection) and then perform your additional configurations on some web server pages hosted by ToM+ itself. Just type in your favorite browser ToM static private IPv4 (***192.188.1.188***) and enjoy!

<figure data-latex-placement="H">
<img src="figures/landing_page.png" style="height:75.0%" />
<figcaption>Web server landing page</figcaption>
</figure>

As you can see in this new version of ToM, the web server is much more complete and user friendly. You can easily navigate through the pages and configure your device as you wish. The web server is also responsive, so you can use it on your smartphone or tablet as well.

### ToM phone application

Along with LCD and black box firmware updates, a minimal Android application is kept updated as well and will allow you to monitor your Twizy real-time data using your smart phone.

The layout tries to emulate the ToM original graphical interface and relies on **MQTT** protocol to share and transfer values from ToM+ to the application, so you will need to configure it both on the app and on ToM+ MQTT page, swapping the IN and OUT topics. The app is distributed with an **APK** file, a packaged installer for Android applications which allow you to mount this app even without an Internet connection. It's available [clicking here](https://www.mediafire.com/file/du7px1bzq0zzdxu/TwizOMeter_v3.1.2.apk/file).

You may need to enable "install apps from unknown sources" flag in your phone settings to open such a file extension *(.apk)*. At first start you may notice a pop-up saying that this application was created for an older version of Android if you have a newer phone: just say OK and ignore it (it will work fine). Some preview of the charging and settings page of the app:

<figure data-latex-placement="H">
<img src="figures/tom_app_charging.png" style="width:80.0%" />
<figcaption>Charging page of the ToM+ Android app</figcaption>
</figure>

<figure data-latex-placement="H">
<img src="figures/tom_app_settings.png" style="width:65.0%" />
<figcaption>Settings page of the ToM+ Android app</figcaption>
</figure>

### Brief consumption overview

ToM will use the 12V battery power supply, taking it directly from the OBD connector and won't consume much, as shown in the progressive measures down below.

<figure data-latex-placement="H">
<img src="figures/consumption_off.png" style="width:65.0%" />
<figcaption>Consumption when Twizy is OFF</figcaption>
</figure>

When the motherboard is active and the display is turned on, it consumes about 90 mA. If the WiFi is turned on as well, the power consumption is around the one shown below (maybe a little more due to the last updates that introduced the 3D graphic).

<figure data-latex-placement="H">
<img src="figures/consumption_on_wifi.png" style="width:65.0%" />
<figcaption>Consumption when ToM+ is ON with WiFi</figcaption>
</figure>

When Twizy is OFF, the black box will go to sleep mode and will consume 18 mA. In addition, the touch capability will allow you to interact much more easily with the device and its LCD display. Since it uses a resistive touch technology, you can use your fingers or a small hard plastic stylus pen to press the buttons. It's not as powerful as capacitive touch screen dashboards but once you have tried it, you can't do without, trust me!

## Provided ToM+ Kit

When ToM+ is shipped, it is usually packaged in a brown box to protect internal boards and sensors from bumps during the travel. In this newer version, no more long cables are needed, just a shorter one connected to the internal ToM+ motherboard, enclosed in a small black plastic container that I usually call "black box". Of course, along with it, the resistive LCD touch display is provided, where you can view and configure all the stuff. No more screws or tape needed! Just an easy clip on display that fits directly on top of the original dashboard.

<figure data-latex-placement="H">
<img src="figures/box.png" style="width:80.0%" />
<figcaption>Provided ToM+ kit</figcaption>
</figure>

### The Black Box

The black box is the motherboard of ToM+ and contains most of the components needed for the system to operate. It provides:

- An external connector for the LCD display;

- An expansion connector with power and GPIO pins;

- An on-board OBD female port for the Twizy CAN bus;

- A microUSB port for firmware updates;

- A female connector for the button on the wiper stalk.

- ON/OFF ToM+ power switch

<figure data-latex-placement="H">
<img src="figures/black_box.jpg" style="width:75.0%" />
<figcaption>The black box</figcaption>
</figure>

### The Expansion Connector

If you would like to customize more your ToM+ you can easily do this using the connector shown in the image here. In fact it gives an additional 5V power supply coming from VCC (ex red cable) and the GND (ex black cable), so that you can power an external LED, a small buzzer or whatever you prefer. The other two cables are General Input Output Pins, PIN1 (ex yellow) and PIN2 (ex blue). They can have either input or output functions, depending on what you will choose on the *"Expansion page"* of ToM **web server**. In this latest version of the device, the expansion connector is embedded in the black box (without colored cables) but the pinout remains the same. Remember to remove the protective cover before using it and to use an input voltage of **maximum 3,3V**. For higher voltage provide a proper resistor divider.

<figure id="fig:expansion_pinout" data-latex-placement="H">
<img src="figures/expansion_bb.jpg" style="width:70.0%" />
<figcaption>Expansion connector</figcaption>
</figure>

### The LCD Display and stand

The resistive touch LCD display is embedded in a 3D printed stand that clips on the original dashboard. If requested, you can also have a 3D standalone support to mount the display on the glovebox as the standard ToM. In that way, you can have a 2 in 1 device that can be both clip-on or standalone as you wish. A microSD slot is accessible for firmware updates.

<figure data-latex-placement="H">
<img src="figures/display.png" style="width:80.0%" />
<figcaption>LCD display clip-on</figcaption>
</figure>

The display, provided with a protective film, as visible in the images, can be put into the 3D container to have an adjustable stand that you can put wherever you like.

<figure data-latex-placement="H">
<img src="figures/3d_stand_wdisplay.png" style="width:80.0%" />
<figcaption>LCD display standalone</figcaption>
</figure>

When inside the standalone version, you can fix it with the cover and the screws that you can find in the packet along with the 3D foldable stand, as shown in the images below.

<figure id="fig:back_cover" data-latex-placement="H">
<img src="figures/back_cover.png" style="width:80.0%" />
<figcaption>LCD cover provided</figcaption>
</figure>

The 3D stand also has holes on the base if you want to screw it on the glovebox. The other holes on the frame are made for screwing the back cover to keep the display in place when inside.

<figure id="fig:bottom_cover_screwholes" data-latex-placement="H">
<img src="figures/bottom_cover_screwholes.png" style="width:80.0%" />
<figcaption>LCD cover screw fixing</figcaption>
</figure>

### Additional Useful Components

The package includes a cable tie to fix the 3D printed stand for the button to the right wiper stalk (included as well). In addition, there is a bonus sticker if you want to support the project by sticking it somewhere on your Twizy.

<figure data-latex-placement="H">
<img src="figures/cable_tie.jpg" style="width:80.0%" />
<figcaption>Cable tie</figcaption>
</figure>

<figure id="fig:wiper_stalk_button" data-latex-placement="H">
<img src="figures/wiper_stalk_button.jpg" style="width:80.0%" />
<figcaption>3D printed button for wiper stalk</figcaption>
</figure>

<figure data-latex-placement="H">
<img src="figures/sticker.png" style="width:80.0%" />
<figcaption>ToM sticker</figcaption>
</figure>

# Installing Twiz O' Meter on Your Car

Installing ToM+ on your Twizy is actually really simple and doesn't need any special knowledge since, as I usually say, it's a "plug and drive" device! So follow this few steps to correctly and quickly install it or try on your own a different location.

## Display LCD position

When ordering the device, you can choose to have the 3D stand along with the clip-on display. So you can choose to install the display in two different ways: using the clip-on mode or using the 3D stand mode. The clip-on mode is the most common and it allows you to attach the display to the car's dashboard, while the 3D stand mode allows you to place the display on a flat surface inside the car (I usually suggest the right or left glove box).

### Clip-on mode

If you choose this mode, it is really simple. You just need to clip the display on the dashboard, in a position that is comfortable for you to see while driving. Put the top part of the display on the dashboard and then push the bottom part until it clicks in place.

<figure data-latex-placement="H">
<img src="figures/clip_on.jpg" style="width:80.0%" />
<figcaption>Clip-on mode installation</figcaption>
</figure>

Make sure that the cable is not pinched in the bottom part of the display but it is free to move in the apposite hole, otherwise you might damage the cable.

### 3D stand mode

If provided, you can use the 3D stand to place the display on a flat surface inside the car. You can put a double-sided tape on the bottom, so you can stick it to the surface. Or you can use the screwholes on the bottom of the stand to fix it with two screws.

As we did for the clip-on mode, make sure that the cable is not pinched in the back part of the display when putting the cover on but it is free to move in the apposite hole, otherwise you might damage the cable. Refer to Figure [1.2](#fig:back_cover){reference-type="ref" reference="fig:back_cover"} and Figure [1.3](#fig:bottom_cover_screwholes){reference-type="ref" reference="fig:bottom_cover_screwholes"} at page  to see the mentioned parts. This is how the 3D stands looks without the display installed.

<figure data-latex-placement="H">
<img src="figures/3d_stand.jpg" style="width:80.0%" />
<figcaption>3D printed empty stand</figcaption>
</figure>

### Cable connection

Then you can remove the protective film from the display and plug in the cable to power it. The other end of the cable needs to be connected to the black box, which will be installed in the next step. It fits only in one way, so make sure to align the connector properly before plugging it in.

<figure data-latex-placement="H">
<img src="figures/bb_connection.jpg" style="width:80.0%" />
<figcaption>Black box connection</figcaption>
</figure>

## Black box position

After you have decided where to place the display, you need to plug in the black box.

The black box needs to be connected to the car's OBD2 port, which is located inside the left glove box of the Twizy. If you've never opened it before, you will find a small plastic cover that you need to remove to access the OBD2 port. Once you have access, simply plug in the black box and make sure it is securely connected. It only fits in one way, so make sure to align the connector properly before plugging it in.

<figure data-latex-placement="H">
<img src="figures/obd_connector.png" style="width:80.0%" />
<figcaption>OBD2 connector location in the Twizy</figcaption>
</figure>

**Only after connecting the display** you can enable the switch on the black box. And the installation is complete! Now you can start your Twizy and enjoy the ToM+ features.

# Basic user interface explanation

## Icon meaning list {#sec:icon_list}

The User Interface (UI) of ToM is really intuitive and easy to use, and each data is represented with a specific icon which usually reminds what that data can be useful for. Here is a list of all icons which you could find on the ToM and their meanings.

### Page icons {#sec:page_icon_list}

Page icons are the icons which you can find on the bottom line of the ToM+ display and they are used to switch between the different pages. Since the last update they have been revamped with a 3D metallic look.

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

### Battery group {#sec:item_numbers}

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

### Charging group

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

### Motor group

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

### Expansion port group

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

### Gyroscope group

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

### Trip group

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

### Dashboard group

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

## Dashboard page

This section will cover the explanation of the dashboard page, which is the main page of the ToM+, so probably the one you will use the most. In the image below I have numbered the most important parts and I will explain each of them in the following paragraphs.

<figure id="fig:dashboard_layout" data-latex-placement="H">
<img src="figures/dashboard_numbers.PNG" style="width:80.0%" />
<figcaption>Dashboard page with numbered parts.</figcaption>
</figure>

**1**

: Current gear of the vehicle, which is usually displayed on the original dashboard as well.

**2**

: A value chosen from torque, power consumption and current consumption, which is used to fill the power bar described in item 6. Tap on the value to cycle between the three options.

**3**

: Error status icon, displayed when an error is present.

**4**

: Shows the active trip. Tap on the icon to open the trip page.

**5**

: Icons for MQTT and WiFi. Greyed out when disconnected, and colored when connected. Tap on the icons if you want to perform a new WiFi scan or a MQTT reconnection.

**6**

: Power bar displaying the selected value from item 2. Starting from the center line, the bar is filled from left to right when accelerating, and from right to left when in regenerative braking. The bar is filled with a color gradient in each direction, and the **maximum and minimum values are customizable** in the web server BigToM page.

**7**

: Displays the instant speed of the vehicle. You can choose between km/h and mph in the web server Advanced Info and Settings page.

**8**

: Motor icon, tap on it to open the motor page.

**9**

: Battery gradient colored icon, tap on it to open the battery info page.

**10**

: Additional displayed values, you can cycle between them by tapping on the icon to change.

**11**

: Displays the time and date, cycle between them by tapping on it.

**12**

: Customizable speed alert limit (green, yellow or red), see Section [4.4.14](#sec:web_btom_tom_sets){reference-type="ref" reference="sec:web_btom_tom_sets"} to enable.

## The pages layout {#sec:main-layout}

The layout can be divided in two main parts, that we will see in detail in the next two paragraphs. The first is the data monitor which has some features to change the data shown in foreground choosing from the ones listed in the side bar. The second is the status icon bar, usually in the bottom of the page. The battery, motor, gyroscope and trip pages share the same layout, shown in the picture.

<figure data-latex-placement="H">
<img src="figures/engine_page.jpg" style="width:80.0%" />
<figcaption>Example of the shared layout (the motor page).</figcaption>
</figure>

In the left side of the screen, as you can see in the photo, there is a list of four values, grouped into a minimal grid. Each value is paired with its measure unit and a small icon, which is unique for each data and all of them were listed in Section [3.1](#sec:icon_list){reference-type="ref" reference="sec:icon_list"}. Above the value there is an orange progress bar which represents how big (or small) is the value compared to its maximum (or minimum) value.\
The right area of the screen is mainly occupied by the foreground data (or simply selected data). It has a big Twizy icon surrounded by an arch shaped progress bar which does the same function of the smaller one discussed before with the only difference that it has 32 steps instead of 16 only. At the edges of the progress bar there is the range or the multiplier of the value shown in the center of the page, which is the one associated with the icon shown just above it.\
In the bottom there is a list of icons, which are used to switch between the different pages of the ToM+. The icons are the same for all pages, and they were all listed in Section [3.1.1](#sec:page_icon_list){reference-type="ref" reference="sec:page_icon_list"}. In the top left corner there is a small icon which shows the current gear of the vehicle. If pressed, **it will take you back to the dashboard page**, we've just discussed. In the top right corner there are three small dots, which if pressed will open the settings page. Lastly, on the long white line at the bottom of the screen, there is the status bar with some icons we will discuss later.

### Changing the foreground data

Changing the data shown in foreground is really easy and intuitive. You can do it just by tapping on the icon of the data you want to show in foreground and the values will swap. In this way you can also rearrange the data in the left side of the screen, which is really useful if you want to have a specific data in an arbitrary order.

<figure data-latex-placement="H">
<img src="figures/change_foreground.jpg" style="width:70.0%" />
<figcaption>Example of changing the foreground data (in the motor page).</figcaption>
</figure>

As an example, in the picture above, the user has tapped on the icon of the motor RPM, which is currently shown in the left side of the screen. The two values have swapped and now the motor RPM is shown in foreground, while the battery SOC is shown in the left grid.

### Changing the active page

To change the active page, you can tap on the icon of the page you want to switch to, which is located in the bottom line of the screen. The icon will become orange and the new page will be displayed. In the image the active page is the motor page.

<figure data-latex-placement="H">
<img src="figures/changing_page.jpg" style="width:70.0%" />
<figcaption>Example of changing the active page (in the motor page).</figcaption>
</figure>

Each of these actions can be performed using the button on the right wiper stalk, which is really useful when driving, since you can keep your eyes on the road and your hands on the steering wheel. The button can be used to cycle between the different pages, to change the foreground data and more. It will be described in detail in Section [4.4.7.5](#sec:web_wiper_stalk){reference-type="ref" reference="sec:web_wiper_stalk"}.

### The status icon bar {#sec:status_icon_bar}

Below the buttons to change page discussed in the previous paragraph, there is a long white line that will show you the network connection status and when alarms or errors trigger as well. At the beginning of the line, as you can see in the picture, is located a small twizy icon with a number: it's a button that will take you to the trip page, that will be discussed later in Section [3.6](#sec:trip_page){reference-type="ref" reference="sec:trip_page"}. Now let's see the status icon bar.

<figure data-latex-placement="H">
<img src="figures/status_icon_bar.jpg" style="width:70.0%" />
<figcaption>The status icon bar.</figcaption>
</figure>

Starting from the right side of the image you will see a magnetic blue wave symbol that stands for the **Wi-Fi** connection status. In fact if it's powered and fixed as it is above it means ToM is connected to a Wi-Fi, which can be both a public network or one from the list you set. When the icon is greyed out ToM is not connected to any networks and will look for Wi-Fi networks again after a cooldown period of five minutes. Or you can force a new scan as soon as possible by tapping on the icon. Last but not least if the icon is blinking ToM has performed a Wi-Fi scan finding one or more networks and is trying to connect to one of them.\
The next icon is a purple cloud with the **"MQTT"** text in it and, as you can guess, stands for the **MQTT** connection status. The position of this icon is fixed and can't be changed, as it is for Wi-Fi one. Another similarity with the previous icon is that can be either fixed or greyed out with the same color code as before.\
Then we have the error icon, which is a red rectangle with the **"ERR"** text in it. It will be displayed when an error is present or hidden when there are no errors.\
Finally we have alarm icons, represented with colored stars. Stars available are the one shown in the picture, you can select which one to use for each alarm in the web server Alarm triggers page. There you can choose whether to make them blink or not.

<figure id="fig:alarm_icons" data-latex-placement="H">
<img src="figures/alarm_icons.png" style="width:70.0%" />
<figcaption>The alarm icons.</figcaption>
</figure>

### Pop-ups

On these pages, pop-ups will appear, depending on your configurations set on the web server "Alarm triggers" page. There are two main types of pop-ups: the first one that won't disappear until you notice and press it (this type will block the whole system, pausing the values in the left grid and the foreground value as well). Otherwise, if you don't want to be bothered while driving you can use the second pop-up type, which was specifically designed to automatically disappear after 10 seconds.\
Here you can see an example of the simplest type of pop-up where the circled warning icon will keep blinking. As you can see it's composed by a yellow box with a dotted outline which contains the icon of the value and the value itself that triggered the alarm previously set on the web server page (motor temperature = 35° C).

<figure data-latex-placement="H">
<img src="figures/pop-up.PNG" style="width:70.0%" />
<figcaption>An example of a pop-up.</figcaption>
</figure>

## The battery info page

The battery info page will give you more detailed info about every single cell of the battery. As you may know standard Twizy batteries have 14 cells and a shared temperature sensor for each couple of them. In this page you are able to monitor each cell voltage and its temperature as well, and you can also have an overview of the full battery voltage. In the image is shown how it usually looks like.

<figure data-latex-placement="H">
<img src="figures/binfo_page.jpg" style="width:80.0%" />
<figcaption>The battery info page.</figcaption>
</figure>

### Checking voltage and temperature

As shown in the image above in the left side of the page is located a battery shaped white line which contains a small table with the first seven cells voltages. To see the remaining cell voltages press the orange and white arrow symbol (the one circled in the next photo) and the grid will show the next values.

If you press the same arrow button again the data shown will change again, becoming the cells temperatures, expressed in Celsius. The foreground value would change as well and as you may notice from the icon above it, showing the full battery temperature, which is the same of each cell in this example. Refer to the image below to see the change.

<figure data-latex-placement="ht">
<figure>
<img src="figures/binfo_page2.jpg" />
<figcaption>Remaining cell voltages.</figcaption>
</figure>
<figure>
<img src="figures/binfo_page3.jpg" />
<figcaption>Cell temperatures.</figcaption>
</figure>
<figcaption>Cell temperatures.</figcaption>
</figure>

### The condensed battery info page {#sec:condensed_binfo}

Pressing the same button again will take you to a special page which contains all the data we discussed in the previous paragraph at once.

<figure data-latex-placement="H">
<img src="figures/binfo_page_condensed.png" style="width:80.0%" />
<figcaption>The condensed battery info page.</figcaption>
</figure>

In the photo above you will see that the screen is divided in two parts. The first one is the same battery shaped white line but a little bigger, in order to contain all voltage and temperature values. The temperature is located between the two cells which share that temperature sensor. In the right side of the page you can see the value that were previously shown in foreground, i.e. the full battery voltage and the full battery temperature. There is also the SOC value in the first position because it's always useful.\
In this page there wasn't enough space to put the buttons to change page, because it's more important to have those status icon we discussed before. If you need to change page you can press the exit button in the bottom right corner and then you will be taken to a page that has the controls to change the active page.\
An important note of the last update is the difference between the cell with the minimum and maximum voltage, respectively represented by a blue and red dot. This value is really important because it can tell you if the battery is healthy or not. If the difference is too high, it means that the battery is unbalanced and it could be a sign of a problem. ToM+ will show you this value in the condensed battery info page, and you can also set an alarm trigger in the web server to be notified when the difference is too high.\
You can decide in the settings whether this condensed battery page is shown as the default page when you press the battery info button or not. The process is shown in Section [3.10](#sec:settings_page){reference-type="ref" reference="sec:settings_page"}. If you select the option to have all the four page we saw in this paragraph, then you can also press the arrow button while on the condensed page to cycle back to the other battery pages info.

## The alarm log page {#sec:alarm_log}

In this page you will be able to see all alarm triggers, if you missed one or if you put them silent not to be disturbed while driving. Let's see how it looks like.

<figure data-latex-placement="H">
<img src="figures/alarm_page.jpg" style="width:80.0%" />
<figcaption>The 3D alarm log page.</figcaption>
</figure>

The image show a small table which contains the item that caused the alarm to trigger paired with its icon and its value. Then I added a date and time as well (available if connected to a network the first time) to know when that record was added to the list.\
In the next images (with the old design), most records are related to the battery SOC, specifically when it goes below the 30%. You will discover how to set your own alarm on the web server in Section [4.4.8](#sec:web_alarm_triggers){reference-type="ref" reference="sec:web_alarm_triggers"}.

<figure data-latex-placement="H">
<img src="figures/alarm_log_old1.png" style="width:70.0%" />
<figcaption>The 3D alarm log page.</figcaption>
</figure>

### Checking older alarm triggers

If you need to see older alarm triggers, which doesn't appear in the list of the first seven ones, then you can press the yellow warning icon at the top of the table, and this will change the values shown with the older ones. You can do this action twice, because ToM is able store up to 21 alarm triggers and forgets older ones.

<figure data-latex-placement="H">
<img src="figures/alarm_log_old2.png" style="width:100.0%" />
<figcaption>Changing the shown triggers.</figcaption>
</figure>

As you can see in these two photos of the alarm log page, when I pressed the circled yellow warning button the data shown changed with some of the older ones as you may notice comparing the dates. The item counter on the left changed as well (8--14).

### Deleting an alarm trigger {#sec:delete_log_record}

If you don't need one or more records anymore, you can choose to delete some of them. Select one or more records to permanently remove by pressing their date or time (a small red check sign will appear next to the chosen records). Then press the trash can icon circled in yellow in the second photo to delete the selected records. Those records will disappear and will be replaced by the next records, causing a shift of the whole list as you may notice in the second picture.

<figure data-latex-placement="H">
<img src="figures/alarm_log_old3.jpg" style="width:100.0%" />
<figcaption>Deleting selected alarm triggers.</figcaption>
</figure>

In this page there aren't any status icon bar or buttons to change page, since it's quite a settings page and doesn't need such controls. To exit, press the arrow button in the bottom right corner and ToM will take you to the page you were before viewing the alarm log page and from that you can change the active page again.

## The trip page {#sec:trip_page}

This page is able to store the data about a trip *(trip means the time from when you start driving to when you power off your Twizy)* and then decide to store or discard these values when you start driving again. You can store simultaneously up to five trip data. The layout is the same as the main page, so the controls to change the order of the values or the data in foreground was already discussed in Section [3.3](#sec:main-layout){reference-type="ref" reference="sec:main-layout"}. Next paragraphs are about how to reset a trip and how to change the current trip.

<figure data-latex-placement="H">
<img src="figures/trip_page_full.jpg" style="width:80.0%" />
<figcaption>The trip page.</figcaption>
</figure>

### Changing the current trip

If you want to start recording the data on a specific trip chosen from 1 to 5 you can press the trip icon circled in yellow in the previous image. When you first press it, you will be taken to the trip nr. 1 and pressing it again and again will cycle through all the available trip, so that you can select the one you would like to start or continue.\
To see in what trip ToM is currently recording refer to the orange number in the trip icon. Once you choose the desired trip you can also change the active page if you want, without losing the selected trip, because ToM will keep recording values even if the trip page is not focused.

### Disable trip recording

In this example I'm currently on the motor page and I'm recording data on the fifth trip page, as it's specified by the small orange number near the trip icon. If you want to pause the trip recording, you can do that on ToM+ by **holding down for three seconds the trip button** while another page is active (in this example the battery one).\

<figure data-latex-placement="ht">
<figure>
<img src="figures/trip_page_on.jpg" />
<figcaption>Trip recording active on trip 5.</figcaption>
</figure>
<figure>
<img src="figures/trip_page_off.jpg" />
<figcaption>Trip recording paused.</figcaption>
</figure>
<figcaption>Trip recording paused.</figcaption>
</figure>

Once you have released it, ToM+ changes the small trip icon showing the map symbol instead of the trip number, to let you know it's not recording data anymore (second picture). When you are ready to start recording the trip again, press on the trip page until you find the desired trip cycling through all the available ones.

### Reset a trip

If you want to clear a specific trip data you can select it and **hold down for three seconds the trip button**. Once you have released it, you should notice that all trip values in the page were reset (tipically to zero). The difference between this action and the previous one is that in this case the trip data is cleared, while in the previous one the trip data is just paused. In addition, here you need to be on the trip page, while in the previous one you should be on any other page.

## The trip history page {#sec:trip_history}

This page stores the data of the last twenty trips and the layout is the same as the alarm log page. The values are updated and stored only when the selected trip is the **number 5**.

### How to access the trip history page

This page is not accessible from the main page, but you can reach it by **long pressing the alarm log icon** in the bottom line of the screen until it changes. This is because the trip history page is not a page you will use often, so it was decided to hide it from the main page to save space, as well as the error page. So, the sequence of pages available by **long pressing the alarm log icon** are: alarm log page (Section [3.5](#sec:alarm_log){reference-type="ref" reference="sec:alarm_log"}) $\rightarrow$ error page (Section [3.8](#sec:error_page){reference-type="ref" reference="sec:error_page"}) $\rightarrow$ trip history page $\rightarrow$ back to alarm log page, each one with the respective icon.\

<figure data-latex-placement="H">
<img src="figures/enter_trip_log_page.jpg" style="width:80.0%" />
<figcaption>The icon to access the trip history page.</figcaption>
</figure>

### Main trip history page controls

<figure data-latex-placement="H">
<img src="figures/trip_history_page.jpg" style="width:80.0%" />
<figcaption>The trip history page.</figcaption>
</figure>

In this image you can see the first seven trips stored in the list, with their date and time, the distance traveled. You can easily change the data shown on each row by pressing on the icon of the data as shown below. The data will cycle between most of the trip data available, so you can choose which one to show. In the next images you can see the same page with the trip power consumption and average speed.

<figure data-latex-placement="ht">
<figure>
<img src="figures/trip_log_kwh.jpg" />
<figcaption>Showing trip power consumption.</figcaption>
</figure>
<figure>
<img src="figures/trip_log_kmh.jpg" />
<figcaption>Showing trip average speed.</figcaption>
</figure>
<figcaption>Showing trip average speed.</figcaption>
</figure>

On the web server you can see all of them at once, it will be discussed in Section [4.4.5](#sec:web_trip_history){reference-type="ref" reference="sec:web_trip_history"}.

## The error page {#sec:error_page}

This page is similar to the alarm log page and the trip history page, but it will show you the last DTC errors that occurred. The controls to delete records or to see older ones was already discussed in Section [3.5](#sec:alarm_log){reference-type="ref" reference="sec:alarm_log"}

### How to access the error page

This page is not accessible from the main page, but you can reach it by **long pressing the alarm log icon** in the bottom line of the screen until it changes. As we discussed before, the sequence of pages available by long pressing the alarm log icon are: alarm log page (Section [3.5](#sec:alarm_log){reference-type="ref" reference="sec:alarm_log"}) $\rightarrow$ error page $\rightarrow$ trip history page (Section [3.7](#sec:trip_history){reference-type="ref" reference="sec:trip_history"}) $\rightarrow$ back to alarm log page, each one with the respective icon.\

<figure data-latex-placement="ht">
<figure>
<img src="figures/enter_error_page.jpg" />
<figcaption>The icon to access the error page.</figcaption>
</figure>
<figure>
<img src="figures/error_page.jpg" />
<figcaption>Showing the error page.</figcaption>
</figure>
<figcaption>Showing the error page.</figcaption>
</figure>

### Main error page controls

As you can see in the second image above, the error page is similar to the alarm log page. It shows a list of the last 14 errors that occurred, with their ODO, the DTC number, the DF number if available, and a representative icon. Refer to the relative page on the web server for more information such as SOC, speed and a brief description (Section [4.4.15](#sec:web_diagnostic){reference-type="ref" reference="sec:web_diagnostic"}).\
By pressing on the icon of the error (circled in yellow in the image) you can cycle between the pages of stored errors, which are 14 in total. The first page shows the last 7 errors, while the second page shows the older ones. To **delete error records** both in this page and on the car, simply click on the trash can icon.\
As in other pages the space wasn't enough to put the buttons to change page, so you can press the exit button in the bottom right corner to go back to the previous page and then change the active one if you want.

## The charging page {#sec:charging_page}

This page doesn't show while driving and there isn't a specific button to view it. That is mainly because this charging screen appears automatically when Twizy is currently in charge state.

As you can see in the image the layout is the same as the dashboard page. The current SOC is shown in the center replacing the speed value.\
An animation will start as well, with a different speed depending on the charging power level. In the photo below there are also some charging specific data, which you can change in the settings as it will be explained later. In this page you don't have the icons status bar, but you still have the network status icons in the bottom right corner, since you can monitor your car charging values when the car is powered off too. In fact, ToM+ will power on automatically when you plug your Twizy into a valid power supply.

<figure data-latex-placement="H">
<img src="figures/charging_page.jpg" style="width:80.0%" />
<figcaption>The charging page.</figcaption>
</figure>

**1**

: Current power stored in the battery, expressed in $kWh$.

**2**

: A value chosen from torque, power consumption and current consumption, which is used to fill the blue part of the power bar. Tap on the value to cycle between the three options.

**3**

: Current charging power, expressed in $kW$, used to fill the right side of the power bar.

**4**

: Shows the ETA, i.e., the estimated time to complete charging.

**5**

: The current SOC, i.e., the state of charge of the battery, expressed in %.

**6**

: Additional displayed values, you can cycle between them by tapping on the icon to change.

**7**

: Icons for MQTT and WiFi. Greyed out when disconnected, and colored when connected. Tap on the icons if you want to perform a new WiFi scan or a MQTT reconnection.

**8**

: Shortcut button to open the settings page, to access more advanced settings.

## The settings page {#sec:settings_page}

In order to let ToM be much more customizable here is the settings page, accessed by pressing the three dots on the top right corner in any of the main pages. Now you can easily edit the basic appearance of your personal ToM.

<figure id="fig:settings_page" data-latex-placement="H">
<img src="figures/settings_page1.jpg" style="width:80.0%" />
<figcaption>The first settings page.</figcaption>
</figure>

The last row will give you info about your personal ToM and will display:

- Your ToM **Serial Number** in the first field (it's censored in the figure above)

- The black box (ESP) firmware version (currently 2.4 in the figure)

- The LCD touch display firmware version (currently 2.4 in the figure)

You can update to the latest version of the firmware as explained in Section [5](#sec:update_procedure){reference-type="ref" reference="sec:update_procedure"}.

### First settings page

As you may notice in the image above, the circled button in the top right corner will tell you which settings page you are currently on. In this case it's the first one, but you can press it to switch to the second one. The first page is mainly about the appearance of the ToM+, while the second one is about the behavior of the ToM+ and some other advanced settings.

#### Customizing page values

If you want to change the order of the data displayed in one of the page or even combine data from different pages you can do it in the settings page, following this steps.

<figure data-latex-placement="H">
<img src="figures/settings_page1_values.jpg" style="width:80.0%" />
<figcaption>Customizing page values.</figcaption>
</figure>

Pressing on the first icon you will cycle between all available pages whose icons were explained before in Section [3.1.1](#sec:page_icon_list){reference-type="ref" reference="sec:page_icon_list"} and will let you customize values for that specific page. In the image above the user has selected the gyroscope page, so the values shown on the right are the ones currently set for that page.\
Each of the five icons under the **Displayed Data** header can be customized just tapping on it, cycling between all data until you find the desired one (icon meaning explained in Section [3.1](#sec:icon_list){reference-type="ref" reference="sec:icon_list"}). For instance you can also choose to put some motor data on the battery page as well, combining the two of them.\

<figure id="fig:icon_arrangement" data-latex-placement="H">
<img src="figures/settings_page1_matching.jpg" style="width:80.0%" />
<figcaption>Resulting layout values.</figcaption>
</figure>

After you have customized the shown values **remember to save by pressing the exit button**. The new configuration will result as shown in the figure: the first data will be the one displayed in the foreground at the center of the page, while all the other ones will be listed in the left side table in the order you specified in the settings page.

#### Choosing the starting page

You can choose which page will be the first one to show when you leave the dashboard page. To do that press the icon to cycle through all available pages until you find the one you want.

In the image below the user has selected the battery page, so when leaving the dashboard page ToM+ will show it first.\

<figure data-latex-placement="H">
<img src="figures/settings_page1_bright.jpg" style="width:80.0%" />
<figcaption>Customizing start page and brightness.</figcaption>
</figure>

#### Adjusting display brightness

As you can see in the image above, you can adjust the display brightness by pressing on the `-` or `+` buttons. The brightness can be set from 0 to 100% and the change will be applied immediately.\

#### Enable/Disable the charging page

ToM+ has a specific page to display more specific charging data (Section [3.9](#sec:charging_page){reference-type="ref" reference="sec:charging_page"}). You can choose whether to keep it enabled (*trust me, it's worth it!*) or disabled.

Tap or slide the button on the left to choose between ON and OFF. When the sliding button is set to ON the ToM will boot up and load the charging page when your Twizy is charging otherwise, in the OFF state it will be switched off while charging. To save your edits press the bottom right corner exit button.\

<figure data-latex-placement="H">
<img src="figures/settings_page1_charge.jpg" style="width:80.0%" />
<figcaption>Customizing charging page and battery kWh.</figcaption>
</figure>

#### Setting your battery capacity

You can set your battery capacity in kWh, which is useful if you have a Twizy with a different battery than the standard one. This will help ToM+ to calculate the remaining range more accurately. You can adjust the value by 0.1 kWh steps by pressing on the `-` or `+` buttons, and the change will be applied immediately. Make sure to **save your new configuration** by pressing the bottom right corner exit button.

#### Calibrating gyroscope module

If you figure out that gyroscope inclination data could be possibly wrong try pressing the "CALIBRATE" button which will perform a gyroscope calibration. Make sure you are **on a plain surface** with your Twizy before doing this operation otherwise your inclination data would be even worse. The process is shown down here:

<figure data-latex-placement="H">
<img src="figures/settings_page1_calibrate.jpg" style="width:80.0%" />
<figcaption>Adjusting gyroscope calibration.</figcaption>
</figure>

#### Changing battery page mode

You can choose whether to have the condensed battery info page only (Section [3.4.2](#sec:condensed_binfo){reference-type="ref" reference="sec:condensed_binfo"}) when you press the battery info button or not.

The two available options are *'Condensed'* and *'Multiple'* and you can switch between them by pressing on the text. The change will be applied as soon as you press the bottom right corner exit button. **Multiple** mode will show all the four battery pages we discussed in Section [3.4.2](#sec:condensed_binfo){reference-type="ref" reference="sec:condensed_binfo"}, while **Condensed** mode will show only the condensed page.\

### Second settings page

This second settings page is about some advanced settings about the charging process. To access it press the circled button in the top right corner of the first settings page and press it again to navigate to the first settings page.\

<figure data-latex-placement="H">
<img src="figures/settings_page2.jpg" style="width:80.0%" />
<figcaption>Second settings page.</figcaption>
</figure>

#### Changing charge level

You can choose the maximum charge level of your Twizy battery, which is useful if you want to limit the power absorbed by the battery to increase its lifetime or for other purposes. The level *'0'* means the limiter is disabled, while the level *'1'* to *'7'* means will use the corresponding charge level up to the maximum available.

To increase or decrease the level press on the `-` or `+` buttons. The change will be applied to the current charge if already charging or to the next charge if not.\

<figure data-latex-placement="H">
<img src="figures/settings_page2_lvl.jpg" style="width:60.0%" />
<figcaption>Changing charge level.</figcaption>
</figure>

#### Manual control of expansion PIN1

Some users reported that would be useful to have a manual control of the expansion PIN1, which is normally used to control an auxiliary charger. So, when needed, you can manually control the expansion PIN1 by pressing the ON/OFF button. The change will be applied as soon as you press the bottom right corner exit button.\

<figure data-latex-placement="H">
<img src="figures/settings_page2_stop.jpg" style="width:80.0%" />
<figcaption>Manual control of expansion PIN1 and stop charge level.</figcaption>
</figure>

#### Stopping the charge at a specific SOC

You can choose to stop the charge at a specific SOC, which is useful if you want to increase the battery lifetime. You can set the value from 0 to 100% by pressing on the `-` or `+` buttons. The change will be applied to the current charge if already charging or to the next charge if not.\

#### Making a max parameters charge

You can choose to make a charge with no power and SOC limits, which is useful if you want once in a while to balance the battery cells. You can press the button to start the max parameters charge, which will be applied to the current charge if already charging or to the next charge if not.\

<figure data-latex-placement="H">
<img src="figures/settings_page2_max.jpg" style="width:80.0%" />
<figcaption>Max parameters charge and abort charging process.</figcaption>
</figure>

#### Abort charging process

You can choose to abort the charging process, which is useful if you want to stop the charge immediately. You can press the button to abort the charge, which will be applied instantly.\

### The right side menu

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

# Advanced ToM+ configurations

## The WiFi settings page {#sec:wifi_settings}

Since the second firmware release, your ToM+ can now connect to the Internet by a Wi-Fi on board module. This will allow you to view your Twizy real time data if combined with MQTT protocol which will be dealt in Section [4.2](#sec:MQTT){reference-type="ref" reference="sec:MQTT"}.\

<figure data-latex-placement="H">
<img src="figures/wifi_settings_3d.png" style="width:80.0%" />
<figcaption>The WiFi settings page.</figcaption>
</figure>

The page will store up to four connection profiles in order to be connected to the Internet when you are at home or even at work or in a public place with a free Wi-Fi.\
In addition ToM+ has a web interface, in which you can monitor data in real time or customize your settings much more easily. Now let's see why you should do this...

### ToM+ WiFi advantages

Since the second firmware release, your ToM+ can now connect to the Internet by a Wi-Fi embedded module and this will allow you to unlock many more features than before. Now you can have access to your Twizy data remotely on your smartphone!\
You won't need to manually check your Twizy charging state anymore, because this new feature will publish charging state data directly on your smartphone and they will be protected and private as well. It will just need some MQTT configuration.\

- No more struggling on constantly checking your Twizy charging state manually!

- Plenty of possibilities to embed your Twizy in an IoT system relying on MQTT

- Wi-Fi would not affect much both electric consumption and ToM performances

- Unlock a new web page with real time Twizy data and ToM user-friendly settings

### Adding a WiFi connection profile {#sec:add_wifi_profile}

In this new settings page you have a small table with four rows and two columns. The first column holds the **SSID** (i.e. the name) of the network you are trying to connect to. To be clear it's the one you see on your phone or laptop. It can be alphanumeric and it is case sensitive (capital letters matter, so be sure to spell it correctly!). While the second column under the **"KEY"** header is for the Wi-Fi password.\
When you tap on a table cell, either SSID or key, ToM+ will open a keyboard page where you can type in your data. Pressing OK will confirm the typed string and will take you back to the Wi-Fi settings page. We will discuss the keyboard page in Section [4.3](#sec:keyboard_page){reference-type="ref" reference="sec:keyboard_page"}.\
By now you are able to set **four different connection profiles** with four pairs of SSID and password. If you don't set any profile but the Wi-Fi slider are enabled ToM+ will still perform a Wi-Fi scan every two minutes trying to find public connection without password protection and then it will try to connect. Press the bottom **right arrow button to save**.\
The fourth WiFi connection profile is special, because the **"KEY 4"** field is used both as a standard password field for the last SSID and to change the default webserver password, as will be discussed in Section [4.4.3](#sec:web_change_password){reference-type="ref" reference="sec:web_change_password"}.

In addition, there are some special codes you can enter in this field to perform some secret configuration. These codes are case sensitive and won't affect your **"KEY 4"** field if written correctly, since ToM+ uses them as commands only. You can type **GIVEMEDF!** (exactly as wrote here, with underscore and exclamation mark too) to *show DF error numbering and error decription* both in display and webUI.\
**REMEMBER!** The commands are executed by ToM+ only if they are entered from this WiFi settings page, not from the webUI discussed later. In addition, since the origin of DF number is not clear, enabling this function is up to you and under your responsibility.

### Check WiFi connection {#sec:check_wifi_connection}

To check if your ToM+ is connected to the Internet via Wi-Fi the process is very simple. In all pages there is the WiFi icon (dealt in Section [3.3.3](#sec:status_icon_bar){reference-type="ref" reference="sec:status_icon_bar"}) which shows its status.

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

If you want to get more specific info about whether or not your ToM+ is connected to any network, you can check additional fields in the Wi-Fi settings page on the bottom right corner, as shown in the image below.

<figure id="fig:wifi_bottom_line" data-latex-placement="H">
<img src="figures/wifi_bottom_line.png" style="width:70.0%" />
<figcaption>The WiFi bottom grid info.</figcaption>
</figure>

As we can see when the ToM+ is connected to a network an IP address will be displayed (here it is **10.24.126.204**). This is the address taken by ToM+ to connect to the Internet. If this field contains any sequence of four numbers (from 0 to 255) separated by dots, then Wi-Fi is connected, otherwise it will be empty.

Tap on it to view ToM+ MAC address and tap again to see which SSID (network name) ToM+ is connected to. We will see more interesting features in which ToM+ IP address is involved later at Section [4.4.2](#sec:web_server_access){reference-type="ref" reference="sec:web_server_access"}.

### Enable/Disable WiFi features {#sec:enable_disable_wifi}

In the footer of the Wi-Fi settings page there are two sliding buttons. To change from ON and OFF state just tap or slide it. Let's see what the two sliders do.\
The first one of them is to disable **Wi-Fi when charging**. This will cause your ToM+ to be completely offline, and you won't be able to monitor your Twizy data remotely until you enable it again. In this state the Wi-Fi status icon will be always grayed out as shown in Section [4.1.3](#sec:check_wifi_connection){reference-type="ref" reference="sec:check_wifi_connection"}.\
The second sliding button is to enable **Wi-Fi when driving**. This will allow your ToM+ to be connected to the Internet even when you are driving your Twizy. This is useful if you want to publish real-time data to your smartphone via MQTT. This also enables the web interface to be accessed while driving and your ToM+ will scan for available Wi-Fi networks as well.\
As already mentioned to *save your changes* you need to press the bottom right arrow button. If you don't do this, your changes will be lost when you leave the page.

## The MQTT settings page {#sec:MQTT}

If you have already took a look at the Wi-Fi Section [4.1](#sec:wifi_settings){reference-type="ref" reference="sec:wifi_settings"}, you would probably now know that MQTT is needed to access to your data remotely and this section will show you how to set up it correctly and how does the ToM+ interface deal with this protocol.

<figure data-latex-placement="H">
<img src="figures/mqtt_settings_page.png" style="width:80.0%" />
<figcaption>The MQTT settings page.</figcaption>
</figure>

When ToM+ is connected to the Internet via Wi-Fi, MQTT can be enabled and then you can view your real time Twizy data directly on your devices. The page only allows only one MQTT server configuration, to ensure **data safety and privacy**. You can configure this parameters both on ToM+ and on its Web Server page (Section [4.4.6](#sec:web_network_settings){reference-type="ref" reference="sec:web_network_settings"}). Now let's discuss what's MQTT and some of its main advantages...

### Brief MQTT explanation {#sec:brief_mqtt}

MQTT is one of the easiest protocols used in IT to communicate small data payloads using a **client/server architecture**. This method requires one or more clients that usually collect data and want to store them permanently and/or perform calculations.

So the process needs a server which processes data from all clients executing tasks. This server is called **MQTT broker** or commonly broker and is essential in this type of architecture. But how can clients and server communicate between themselves?\
The communication process is based on a publish/subscribe structure. Some clients collect and publish data and for this reason they are called **publishers** and, in the meanwhile some others wait for those data to be sent and they're called **subscribers**. The broker server lays in the middle and is the intermediary device on which all data from publishers are stored and sent to subscribers. Now let's introduce topics...\
A **topic** is a sequence of alphanumeric characters typically related to a specific subject and it's used to store (like a container) all data related to that specific subject. Topics are useful to keep and organize a lot of data collected from different publishers in order not to confuse those information. So, how ToM+ uses MQTT?

### ToM+ and MQTT communications

Now that we know what's MQTT, let's see how MQTT and ToM+ system actually works. ToM+ is considered a publisher, because it collects and publishes Twizy updated data. The phone application instead, will be the subscriber because it is waiting to receive those data that the Twizy has just published. But who is in the middle? The broker server.\
Unless you have a self-hosted broker server (as I do), or you already know one to use, I will explain how to set up your free external broker server in Section [4.2.3](#sec:free_broker){reference-type="ref" reference="sec:free_broker"}.

So, combining ToM+ with MQTT protocol can be very powerful and if you like home automation and IoT systems can also unlock endless possibilities. For instance, you can create your own subscriber that will perform actions on ToM+ published data.\

### Setting up MQTT free broker {#sec:free_broker}

*Disclaimer*: Take your time while doing this process because for not expert users may take some more minutes and be sure to **note down your configuration** parameters.\
First of all choose your MQTT broker provider, I personally advice Maqiatto, since it's free, intuitive and easy to use. So let's visit the official website tutorial page: <https://www.maqiatto.com/examples>. Now we should see a page like the one shown here:

<figure data-latex-placement="H">
<img src="figures/mqtt_step1.png" style="width:100.0%" />
<figcaption>Step 1: Press “CREATE ACCOUNT” button.</figcaption>
</figure>

As the official guide says, you need to have an account in order to create your MQTT broker. So let's press the top right circled **"Create Account"** button and create one. You will be redirected to this page (<https://www.maqiatto.com/signup>) where you will have to fill in your personal data.

<figure data-latex-placement="H">
<img src="figures/mqtt_step2.png" style="width:100.0%" />
<figcaption>Step 2: Fill in your personal data.</figcaption>
</figure>

After filling in all the form fields press the **"Signup"** green button and wait until we get this page (<https://www.maqiatto.com/configure>) popping up a successful registration message as shown in the image down here:

<figure id="sec:free_broker_add_topics" data-latex-placement="H">
<img src="figures/mqtt_step3.png" style="width:100.0%" />
<figcaption>Step 3: Add IN/OUT topics.</figcaption>
</figure>

From this page you can manage your available topics (refer to Section [4.2.1](#sec:brief_mqtt){reference-type="ref" reference="sec:brief_mqtt"}) and creating new ones as well. So let's create our IN and OUT topic for sending and receiving ToM data. As we can see, there's a fixed prefix (your email) since free users have this limitation, but it isn't a problem at all.\
In the blank text box after the "/" symbol we should put the name we want to give to our topics. Choose it carefully and make sure it is clear and easy for you to remember. For instance I will call the input topic **TOMin** and the output topic **TOMout**, but you can choose the name you prefer.\
For the first topic, type **TOMin** and press the **"+ Add Topic"** blue button as I did above. If the operation ends up correctly then a green popup message will show, saying **"Topic was added for this user"** and a new records will appear in the *"Available Topics"* list that was empty before. Now repeat the process for the **TOMout** topic as well and check again if the topic was successfully created. Before this process the *"Available Topics"* list was empty, but now we can see our two topics in the list and we can delete them if needed.

<figure data-latex-placement="H">
<img src="figures/mqtt_step4.png" style="width:80.0%" />
<figcaption>Step 4: Change your broker password.</figcaption>
</figure>

*This step is suggested but optional*. At this point the broker password is the same of your Maqiatto account and it is not secure at all. But if you don't want to change it or you don't care, you can skip this step and go to the next one.\
So let's take some time to make the broker secure and protected from unwanted access. The second part of this page (<https://www.maqiatto.com/configure>) allows you to change your broker password. Just type the new one in the **"New MQTT Password"** text field and then press the **"Change Password"** blue button.

If everything goes well, a green popup message will show up saying **"Broker user password was updated"**. The change username button is greyed out because you can't change your username unless you are a premium user.

<figure data-latex-placement="H">
<img src="figures/mqtt_step5.png" style="width:70.0%" />
<figcaption>Step 5: Note down the port number.</figcaption>
</figure>

In the last section of the configuration page (<https://www.maqiatto.com/configure>) there are the **"Port Management"** parameters. Note down the MQTT TCP Port which is usually set to **1883** (just to be sure) because it's the standard well-known port number over the Internet for MQTT protocol. Now the MQTT broker is ready to be used and we can move on to the next step, which is configuring ToM+ with the broker parameters.

### Connect ToM+ to MQTT broker {#sec:mqtt_connection}

Now that it's clear what MQTT (Section [4.2.1](#sec:brief_mqtt){reference-type="ref" reference="sec:brief_mqtt"}) is and we have set up our personal broker (Section [4.2.3](#sec:free_broker){reference-type="ref" reference="sec:free_broker"}) let's see where on the display we can connect ToM+ with our freshly created broker.

<figure data-latex-placement="H">
<img src="figures/mqtt_connect1.png" style="width:80.0%" />
<figcaption>MQTT broker connection parameters.</figcaption>
</figure>

When you tap on the respective table field, ToM+ will open a keyboard page where you can type your data, as in Wi-Fi settings. To insert the symbols or numbers press the **"1/3"** button on the keyboard to switch charset. By pressing **OK**, you will confirm the typed string and will take you back to the MQTT settings page. To know more about the keyboard page see Section [4.3](#sec:keyboard_page){reference-type="ref" reference="sec:keyboard_page"}. If the value is too long for the field, the text would automatically scroll.\
The first thing to specify is your **broker address**. In the example shown, it's set to *"maqiatto.com"*. This is the address of the broker server that we have just created in Section [4.2.3](#sec:free_broker){reference-type="ref" reference="sec:free_broker"}.

Then it's time to specify the **port number** where the MQTT service is running. Unless you have set it to a different number manually the MQTT port will always be *1883*.

Next we have the **user** field, which is the username that ToM+ will use to authenticate when connecting to the broker. Since the pair of username and password is unique to you, this will prevent unwanted user to have access to your private broker. In your case, the user is your Maqiatto account e-mail, written like *youremail@example.com*.

Afterwards we need to specify the **password of the broker** which can be different from the one of your Maqiatto account if you chose to change it when suggested in Section [4.2.3](#sec:free_broker){reference-type="ref" reference="sec:free_broker"}.

<figure data-latex-placement="H">
<img src="figures/mqtt_connect2.png" style="width:80.0%" />
<figcaption>MQTT ToM+ publishing parameters.</figcaption>
</figure>

Now let's configure our **OUT topic**, where ToM+ will publish Twizy data. In Section [4.2.3](#sec:free_broker){reference-type="ref" reference="sec:free_broker"} we created an out topic called TOMout but the full name of the topic must include also **your e-mail as a prefix** followed by a "/" symbol and the topic name "TOMout". In the example it is set to *"youremail@gmail.com/TOMout"*.

Now it's time for the **IN topic**, where ToM+ will receive MQTT commands. As for the OUT topic, we created an in topic called TOMin but the full name of the topic must include also **your e-mail as a prefix** followed by a "/" symbol and the topic name "TOMin". In the example it is set to *"youremail@gmail.com/TOMin"*.

When an MQTT publisher sends a message to the broker its connection is authenticated by username and password but it publishes using an alias which *you can arbitrarily choose*. It's important not to include spaces in the **Client ID**, only alphanumeric characters and symbols are allowed. Remember that it's advisable to make it simple and clear as it is in the example: *"TwizOMeter"*.

The last parameter is the **publish frequency**, which represents the time between each ToM+ publish. It's expressed in milliseconds *(ms)* and can be set to an arbitrarily value greater than 1000ms (one second). The default is *5000 ms* (five seconds) and it is a good compromise between data freshness and network usage.\
To **save your changes** you need to press the bottom right arrow button. If you don't do this, your changes will be lost when you leave the page. Now ToM+ is ready to publish and receive data via MQTT protocol.\

### Enable/Disable MQTT features {#sec:enable_disable_mqtt}

If you want to temporarily or permanently disable the publishing of data with MQTT protocol press or slide on the left slider called **"PUBLISH"** in the image down here. From then on ToM+ won't publish Twizy data via MQTT until you enable it again.

<figure data-latex-placement="H">
<img src="figures/mqtt_connect3.png" style="width:80.0%" />
<figcaption>MQTT bottom sliders.</figcaption>
</figure>

The right slider button under **"SUBSCRIBE"** allows ToM+ to receive commands from external devices published on the specified IN topic. This is useful if you want to control via MQTT a device connected to ToM+ expansion port (e.g. a smart plug to turn on/off charging remotely). You can choose to enable or disable this feature at any time by pressing or sliding the button.\

### Check ToM+ MQTTconnection

Near the two sliding buttons, there's a small **"STATUS"** label which holds wheter the MQTT connection is working or not. When ToM+ is connected to the MQTT specified broker, you will see a *"CONNECTED"* text. When there's a problem with the broker connection or Wi-Fi is disabled, as we saw in Section [4.1.4](#sec:enable_disable_wifi){reference-type="ref" reference="sec:enable_disable_wifi"}, MQTT won't work properly and a *"DISCONNECTED"* message appears as in the image below.

<figure data-latex-placement="H">
<img src="figures/mqtt_status.png" style="width:80.0%" />
<figcaption>MQTT status field.</figcaption>
</figure>

By the way you can check the MQTT connection status also by looking at the status icon bar (Section [3.3.3](#sec:status_icon_bar){reference-type="ref" reference="sec:status_icon_bar"}) where the MQTT icon will be purple if the connection is established, otherwise it will be grayed.

To **save your changes** you need to press the bottom right arrow button. If you don't do this, your changes will be lost when you leave the page.\

## The Keyboard page {#sec:keyboard_page}

When you tap on a table cell in the Wi-Fi or MQTT settings page, ToM+ will open a keyboard page where you can type in your data. The keyboard page is very intuitive and easy to use. You can switch between three different charsets by pressing the **"1/3"** button on the bottom left corner of the keyboard.

<figure data-latex-placement="ht">
<figure>
<img src="figures/keyboard_page1.jpg" />
<figcaption>First charset: Letters.</figcaption>
</figure>
<figure>
<img src="figures/keyboard_page1_caps.jpg" />
<figcaption>First charset: Uppercase letters.</figcaption>
</figure>
<figcaption>First charset: Uppercase letters.</figcaption>
</figure>

In the **first charset**, you can type letters in lowercase or uppercase by pressing the shift button circled in yellow in the first image. When you type something it will appear in the text field on the top of the keyboard. If you want to delete a character just press the backspace button.

<figure data-latex-placement="ht">
<figure>
<img src="figures/keyboard_page2.jpg" />
<figcaption>Second charset: Symbols.</figcaption>
</figure>
<figure>
<img src="figures/keyboard_page3.jpg" />
<figcaption>Third charset: Numbers and more.</figcaption>
</figure>
<figcaption>Third charset: Numbers and more.</figcaption>
</figure>

The **second charset** is for symbols and the **third one** is for numbers and other special characters. To move to the third charset just press the **"2/3"** button on the bottom left corner of the keyboard. When on the third charset, you can switch back to the first charset by pressing the **"3/3"** button. In these two pages the shift button won't do anything because it is not needed.\
When you are done typing, press the **OK** button to confirm your input and return to the previous MQTT or WiFi settings page, where the edited field will be updated.

### The number-only keyboard

In some fields, such as the MQTT publish frequency, only numbers are allowed. In this case, ToM+ will open a number-only keyboard page as shown in the image below.

<figure data-latex-placement="H">
<img src="figures/keyboard_num_only.jpg" style="width:80.0%" />
<figcaption>Number-only keyboard.</figcaption>
</figure>

As you can see, the layout is the same as the third charset of the full keyboard, but it is limited to numbers and a few special characters. You can also notice that the change charset button is unavailable, as it is not needed in this case. The backspace button is still available to delete characters, and the **OK button** confirms your input and returns to the previous page.

## The web server {#sec:web_server}

The web server is a new feature introduced with the second firmware release. It allows you to access your ToM+ settings and data remotely from any device with a web browser, such as your smartphone, tablet, or PC. This is particularly useful for managing standard and **advanced configurations** that aren't available on the ToM+ display.

In addition, you can also use the web server to set up **WiFi and MQTT** much more easily than using the ToM+ display with the keyboard page only (Section [4.3](#sec:keyboard_page){reference-type="ref" reference="sec:keyboard_page"}).\

<figure data-latex-placement="H">
<img src="figures/landing_page.png" style="width:46.0%" />
<figcaption>Landing page of the web server.</figcaption>
</figure>

### The landing page

In the landing page shown above, you will see twelve buttons that give you access to different pages of the web server. Here I will give a quick overview of the functions available on each page and then in the next paragraphs they will be all deepen more. In these section, the icons are used as a visual aid only:\

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

### Access the web server {#sec:web_server_access}

ToM+ allows you to connect to its web server page in two ways, and they are both useful in different situations. Before we start, bear in mind that an **IP address** it's basically the numeric name of your device on a network (e.g. *192.168.1.100*).

***For both methods, you need ToM+ to be connected to a network.*** So, be sure to check if your ToM+ has either a Wi-Fi profile configured as explained in Section [4.1.2](#sec:add_wifi_profile){reference-type="ref" reference="sec:add_wifi_profile"} or is connected to a no-password WiFi network. To check if your ToM+ is connected please refer to Section [4.1.3](#sec:check_wifi_connection){reference-type="ref" reference="sec:check_wifi_connection"}.\
**The first and easier setup** is using your phone hotspot without any password, so that ToM+ connects without having to configure any WiFi profile. Then, still using your phone, go on Chrome or Safari (or any web browser) and type in ToM+ IP address (shown as Figure [4.1](#fig:wifi_bottom_line){reference-type="ref" reference="fig:wifi_bottom_line"}).\
**The second method** works only when you are quite near to the Twizy within WiFi range. You can use your phone or laptop to perform a WiFi scan and then search for either *"ToM+ AP"* or *"Twiz o'Meter AP"* or *"BigToM AP"* network, depending on your model. Next, you should connect to that network with the **correct password**. It is initially set to the word "pass" followed by your device serial number (e.g. *pass129777*). Serial number can be found in the settings page as explained in Figure [3.3](#fig:settings_page){reference-type="ref" reference="fig:settings_page"}. Then you can change it if you want, but there's no password recovery system (see Section [4.4.3](#sec:web_change_password){reference-type="ref" reference="sec:web_change_password"}). Once you are connected to ToM+ Access Point, type on any browser his static IP address, which is **192.188.1.188**.

### Change web server password {#sec:web_change_password}

To change the password for the web server, go on the display WiFi settings page (Section [4.1](#sec:wifi_settings){reference-type="ref" reference="sec:wifi_settings"}) and tap on the **"KEY 4"** field. This will open the keyboard page (Section [4.3](#sec:keyboard_page){reference-type="ref" reference="sec:keyboard_page"}) where you can type in your new password. So, this password will be used for both the Access point password as well as the fourth WiFi connection profile.

### Data monitor page {#sec:web_data_monitor}

As said in the introduction, this page lists all available ToM+ data, organized into seven different tables, each of which contains only the data specified in its header. The data distribution is the same used in Section [3.1](#sec:icon_list){reference-type="ref" reference="sec:icon_list"} and can't be modified.

These values are **updated every 10 seconds** and are coupled with their measure unit. Don't worry for your privacy because your data travels packed in a particular packet structure that is difficult to sniff or crack. In addition, the web server does not use any external services or MQTT for the monitoring so that your data remains private and safe. The page is fully generated directly by the black box and doesn't undergo any further processing.

<figure data-latex-placement="H">
<img src="figures/monitor_page1.png" style="width:100.0%" />
<figcaption>Data monitor page — top tables.</figcaption>
</figure>

In the second part of the page, there are the last three tables which contain dashboard data, expansion port data and the last one holds all the battery info voltages and temperatures. Press the **"HOME"** green button pointed by the red arrow to return to the landing page.

<figure data-latex-placement="H">
<img src="figures/monitor_page2.png" style="width:100.0%" />
<figcaption>Data monitor page — bottom tables.</figcaption>
</figure>

### Trip history page {#sec:web_trip_history}

This holds the values of the trip page previously discussed in Section [3.6](#sec:trip_page){reference-type="ref" reference="sec:trip_page"}. It can store up to 5 different sets of data and, even if display shown data are limited, the web server page will show them all. The first table shows trips, each organized into five rows and the headers of each record are listed in Section [3.1](#sec:icon_list){reference-type="ref" reference="sec:icon_list"}.

<figure data-latex-placement="H">
<img src="figures/trip_page1.png" style="width:100.0%" />
<figcaption>Trip history page — Trip data.</figcaption>
</figure>

The second table shows the last twenty trips (from the most recent), with the same headers as the first table. You can get back to the start page pressing the **"HOME"** green button located just below the second table.

<figure data-latex-placement="H">
<img src="figures/trip_page2.png" style="width:100.0%" />
<figcaption>Trip history page — Trip history.</figcaption>
</figure>

### Network settings page {#sec:web_network_settings}

This page allows you to configure Wi-Fi profiles and MQTT broker without struggling with the ToM+ display keyboard. The page is split in two main tables, one for Wi-Fi (Section [4.1](#sec:wifi_settings){reference-type="ref" reference="sec:wifi_settings"}) and the other for MQTT settings (Section [4.2](#sec:MQTT){reference-type="ref" reference="sec:MQTT"}).\
As you can see in the image the first one contains all the four profiles that were previously set on ToM+, or if not, their default values. The same is for passwords, that are not visible until you press the "O" button next to the one you want to see. Pressing it again will hide the password. Here you can also change the Wi-Fi password for the Access Point (Section [4.4.3](#sec:web_change_password){reference-type="ref" reference="sec:web_change_password"}).

<figure data-latex-placement="H">
<img src="figures/wifi_page1.png" style="width:100.0%" />
<figcaption>Network settings page — WiFi table.</figcaption>
</figure>

The two check boxes do the same functions as the two sliding buttons in ToM+ WiFi settings page. To know what they are used for, refer to Section [4.1.4](#sec:enable_disable_wifi){reference-type="ref" reference="sec:enable_disable_wifi"}. After any change, press the **"SAVE"** button to save your changes, otherwise they will be lost when you leave the page.

<figure data-latex-placement="H">
<img src="figures/wifi_page3.png" style="width:100.0%" />
<figcaption>Network settings page — WiFi status table.</figcaption>
</figure>

If your ToM+ is connected to a network, a small table will appear below the one just discussed and the rows contain three main information: the SSID, ToM+ IP address and the MAC address. These data can be found on the ToM+ display as well, in the Wi-Fi settings page as previously shown in Figure [4.1](#fig:wifi_bottom_line){reference-type="ref" reference="fig:wifi_bottom_line"}.\
The second main table, instead holds the MQTT broker settings, as they were previously configured on ToM+ display, or if not, default values (*e.g. "broker.address"*). You can easily change them manually from this web server page, that is much more comfortable than using the ToM+ display keyboard. Check below in the image how this table may look once configured.

<figure data-latex-placement="H">
<img src="figures/wifi_page2.png" style="width:100.0%" />
<figcaption>Network settings page — MQTT table.</figcaption>
</figure>

The two check boxes do the same functions as the two sliding buttons in ToM+ MQTT settings page. To know what they are used for, refer to Section [4.2.5](#sec:enable_disable_mqtt){reference-type="ref" reference="sec:enable_disable_mqtt"}. If your ToM+ is connected to the MQTT broker, the table header will have a **"(CONNECTED!)"** text.\
After any change, press the **"SAVE"** button to save your changes, otherwise they will be lost when you leave the page. At the end of this page, pointed by a red arrow in the image, there's the **"HOME"** green button to return to the landing page.

### Expansion settings page {#sec:web_expansion_settings}

This page holds the configuration for PIN1 and PIN2 of the expansion connector, as well as the configuration for the right wiper stalk button. It can be really useful if you like customizing stuff and adding your personal touch to your ToM+. The pin-out of the expansion connector is shown in Figure [1.1](#fig:expansion_pinout){reference-type="ref" reference="fig:expansion_pinout"}. Since they are general input/output pins you can choose the mode of each one depending on your needs.\
If you choose the **"INPUT"** mode, then that line will be listening to the signal specified in the next field, and this can be really useful when setting a really specific alarm, but we will discuss this later. On the other hand, if you select the **"OUTPUT"** mode ToM+ will transmit the signal specified in the next field, which can be HIGH (5V) or LOW (0V), when an alarm triggers. But as said before, it will be depth in Section [4.4.8](#sec:web_alarm_triggers){reference-type="ref" reference="sec:web_alarm_triggers"}.\
Since the most recent firmware releases, new modes other than INPUT and OUTPUT have been added to the expansion PINs. Let's dig into them:\

- **IR CONTROLLER**: This mode allows ToM+ to be controlled by an infrared remote.

- **KEY+ CONTROLLER**: This mode allows you to control your ToM+ via a rotational infrared remote. For these two first modes an additional configuration table will appear.

- **SERIAL TX**: Allows you to configure a serial TX line (still not implemented).

- **SERIAL RX**: Allows you to configure a serial RX line (still not implemented).

- **CTRL BUTTON**: This mode allows you to use the right wiper stalk button as a control button for your ToM+ gestures.

#### Standard OUTPUT mode

Both in **"OUTPUT"** and **"INPUT"** mode, you will need first of all to choose between *"Active High"* or *"Active Low"*. When an alarm triggers a LOW/HIGH signal is sent to the PIN chosen as the alarm output (either PIN1 or PIN2).

If you select *"Active High"*, the signal sent is HIGH (5V) and normally is held to LOW (0V).

If you select *"Active Low"*, the signal sent is LOW (0V) and normally is held to HIGH (5V).

<figure data-latex-placement="H">
<img src="figures/expansion_page1.png" style="width:100.0%" />
<figcaption>Expansion settings page — PIN1 table.</figcaption>
</figure>

As you can see in the image below, when selecting the **"OUTPUT"** mode, you can also choose the *"Output Type"*. This is useful if you have a really specific output device that needs additional management that is not limited to the standard HIGH/LOW signal. To achieve this, you can choose from a list of already managed output devices, highlighted in the image above.\
After any change, press the **"SAVE"** button to save your changes, otherwise they will be lost when you leave the page. If you got an idea for a new output device that can be useful for the community, feel free to contact me.\

- *"Normal"*: This is the standard OUTPUT mode, limited to HIGH/LOW signals.

- *"Charger auxilliary fan"*: This lets you control an auxilliary fan. You will need to set an alarm on charger temperature with a threshold. Then, when charging, if it triggers the fan will start cooling the charger, stopping only after the temperature drops below the selected threshold with a fixed hysteresis (even after charging is finished if needed).

- *"Reku break light"*: This lets you connect a relay board which controls the breaking light, in order to power it on when in regeneration mode. This is particularly useful if your Twizy is tuned to increase the regeneration power.

- *"Auxilliary charger"*: This lets you control an auxilliary charger with an alarm on SOC or battery voltage. It lets you connect a relay board that enables or disables an auxilliary charger when needed. It powers on only in charging mode, with a small fixed delay.

- *"Motor fan"*: This lets you control a motor fan with an alarm on the engine temperature. It works the same as the charger fan with the difference that this works only while driving.

#### Standard INPUT mode

As you can see in the image below, when selecting the **"INPUT"** mode, no additional tables will appear. This mode heavily relies on alarm configuration and triggers, so plese refer to Section [4.4.8](#sec:web_alarm_triggers){reference-type="ref" reference="sec:web_alarm_triggers"}. We chose **"INPUT"** mode in the second table, that works the same but it's intended for PIN2 of the expansion connector.

After any change, press the **"SAVE"** button to save your changes, otherwise they will be lost when you leave the page.

<figure data-latex-placement="H">
<img src="figures/expansion_page3.png" style="width:100.0%" />
<figcaption>Expansion settings page — PIN2 table.</figcaption>
</figure>

#### IR CONTROLLER mode

First of all you will need an IR receiver (either a sensor or a module like the one in the first image) to be plugged in one of the expansion board PINs. This mode is intended to be used with a general IR remote, but the one I personally suggest is the one shown in the second image below, specially designed to be put on the steering wheel.

<figure data-latex-placement="ht">
<figure>
<img src="figures/ir_receiver.jpg" />
<figcaption>IR receiver module.</figcaption>
</figure>
<figure>
<img src="figures/ir_controller_photo.jpg" />
<figcaption>IR controller steering wheel remote.</figcaption>
</figure>
<figcaption>IR controller steering wheel remote.</figcaption>
</figure>

When you select the **"IR CONTROLLER"** mode for either PIN1 or PIN2 table, remember to press the **"SAVE"** button to save your changes. Once you saved, the page will reload and an additional table will appear below, you can see it in the image below.

<figure data-latex-placement="H">
<img src="figures/ir_settings.png" style="width:80.0%" />
<figcaption>Expansion settings page — IR settings table.</figcaption>
</figure>

This table will help you to pair each button of the IR controller with the respective IR code. In the top part of the table there is a little text area that you can use as an **IR code receiver moditor** to test in real-time IR codes of your remote after plugging the IR receiver.\
Using this, you can fill the other fields accordingly. The last one is particularly important and it's basically the code the remote sends when you are holding down a button. After that, remeber to press the **"SAVE"** button to save your changes, otherwise they will be lost when you leave the page. Lastly, a useful **"Default"** button is located next to it, to easily revert your changes if needed.

#### KEY+ CONTROLLER mode

This mode is really similar to the one just discussed, but is intended to be used with another type of controller (the one in the picture below). It's a Bluetooth wireless rotary controller for car audio systems, which performs different actions depending on how fast/slow you are rotating the external ring. And of course it has some more buttons as well in the internal part.\

<figure data-latex-placement="H">
<img src="figures/keyp_controller.jpg" style="width:40.0%" />
<figcaption>Bluetooth wireless rotary controller.</figcaption>
</figure>

When you select the **"KEY+ CONTROLLER"** mode for either PIN1 or PIN2 table, remember to press the **"SAVE"** button to save your changes. Once you saved, the page will reload and an additional table will appear below, you can see it in the image below.

<figure data-latex-placement="H">
<img src="figures/keyp_settings.png" style="width:80.0%" />
<figcaption>Expansion settings page — KEY+ settings table.</figcaption>
</figure>

This works the same as the IR settings table. The main difference is about what ToM+ reads from the expansion port, that is not an IR code anymore: it's a voltage instead.

In the image above are shown the default values, ranging from *0* to *3.3V* written without the decimal dot symbol. For example, *018* means *0.18V* and *157* is *1.57V* and so on. ToM+ has a tolerance of *0.05V* on input values to avoid voltage bouncing.\
After that, remeber to press the **"SAVE"** button to save your changes, otherwise they will be lost when you leave the page. Lastly, a useful **"Default"** button is located next to it, to easily revert your changes if needed.

#### CTRL BUTTON mode {#sec:web_wiper_stalk}

This last table holds the configuration needed to make the provided right **wiper stalk button** (Figure [1.4](#fig:wiper_stalk_button){reference-type="ref" reference="fig:wiper_stalk_button"}) work. You can use this button to navigate through all ToM+ UI without using the touch-screen, with these three main **actions**: *"Browse items"*, *"Change page"*, *"Select-deselect"*. To achieve this, there are three type of **button presses**: *"Short"*, *"Medium"*, *"Long"*.\

<figure data-latex-placement="H">
<img src="figures/expansion_page2.png" style="width:100.0%" />
<figcaption>Expansion settings page — Wiper stalk button table.</figcaption>
</figure>

So, in the first part of this table you can rearrange this actions with the gestures you prefer.\

- *"Browse items"*: This moves a small white marker next to the current selected data.

- *"Change page"*: This lets you cycle through the pages present in the rotation.

- *"Select-deselect"*: This simulates tapping on the selected data (e.g. switches from background to foreground).\

In the second part of the table you can select the **pages you would like to skip** when cycling through the available pages repeating the *"Change page"* gesture. For instance, if I don't want to monitor the Info battery page when cycling with the button, I just check it out and it will be removed from the rotation.\
After any change, press the **"SAVE"** button to save your changes, otherwise they will be lost when you leave the page. At the end of this page, pointed by a red arrow in the image, there's the **"HOME"** green button to return to the landing page.

### Alarm triggers page {#sec:web_alarm_triggers}

When something happens on ToM+ and you want to get noticed about it, you can choose how to be notified and when in this page. You can have up to **ten alarms** running simultaneously and TOM+ constantly checks the state of each condition. In the image is shown the first table, where you can see currently active alarms.

<figure data-latex-placement="H">
<img src="figures/alarm_page1.png" style="width:100.0%" />
<figcaption>Alarm page — Existing alarms list table.</figcaption>
</figure>

The headers of the tables are practically the elements of the condition that ToM+ listens for.\

- **ITEM**: This is the data to be checked, chosen from the list of Section [3.1](#sec:icon_list){reference-type="ref" reference="sec:icon_list"}.

- **CONDITION**: This is the operator sign used when comparing the values.

- **VALUE**: This is a signed integer value used as the second term of the comparison.

- **ACTION**: This is the action performed when the alarm triggers. See the next table.

- **SEND-MQTT**: This is a binary field and if crossed, pulish a message on MQTT topic.

- **COMMAND**: This is an optional string to be sent as an additional command.

 \
The first alarm trigger checks the battery consumption and activates the PIN2 of the expansion board if it's greater than 35A. In this specific example, it is used to power on the rear brake light when the regeneration is enough to make the Twizy slow down.\
The second alarm trigger checks the battery SOC and shows on the display a simple pop-up that notify that the battery level is lower than 30%. By checking the *"Change page"* field, I added a further option that will tell ToM+ to send a MQTT message when this alarm triggers.\
The third alarm trigger checks the battery SOC and once charge is complete, e.g. equal 97%, it does the same as before but performs an additional command. The command *cmd/charge/Power 0* disables a Tasmota Wi-Fi switch that connects the Twizy plug to the wall socket.

So, the function of the **"COMMAND"** column is really useful and allows you to embed your ToM+ in your IoT house. See the Appendix [7](#apx:tasmota){reference-type="ref" reference="apx:tasmota"} for detailed configurations.\
When you want to remove a specific alarm you will just need to press the **"Remove"** button in its last column.\

<figure data-latex-placement="H">
<img src="figures/alarm_page2.png" style="width:100.0%" />
<figcaption>Alarm page — Adding new alarm table.</figcaption>
</figure>

In the second table you can add a new alarm to the list we have just discussed. First of all you have to choose the **ITEM**, between all the available data listed in Section [3.1](#sec:icon_list){reference-type="ref" reference="sec:icon_list"}. In this choice box items are organized as in the list just quoted. Then select the **CONDITION**, i.e. the operator of the comparison, between *"lower"*, *"greater"* or *"equal"*. Next it's time for the reference **VALUE**, a signed integer number, the right term of the comparison.\
Let's take some time to explain all of the possible **ACTION**s.\

- *pop-up*: a yellow pop-up notifying the item value appears in the center of the screen. To hide it just press it once. You can see a pop-up example in the first image below.

- *pop-up 10 sec*: a yellow pop-up notifying the item value stays on the screen for ten seconds.

- *silent*: no visible actions happen: it's commonly used to post MQTT messages only.

- *icon x fix*: icon x (*where x can be 2,3,4 or 5*) lights on. See Figure [4.4](#fig:alarm_icons2){reference-type="ref" reference="fig:alarm_icons2"} for alarm icons.

- *icon x blink*: icon x (*where x can be 2,3,4 or 5*) starts blinking.

- *pin1 active*: PIN1 of the expansion board gets activated (LOW or HIGH depending on the level selected in the expansion settings page in Section [4.4.8](#sec:web_alarm_triggers){reference-type="ref" reference="sec:web_alarm_triggers"}).

- *pin2 active*: PIN2 of the expansion board gets activated. In this example PIN2 was set as INPUT mode so it's greyed out, because it can't represent an OUTPUT action.

 \

<figure id="fig:alarm_icons2" data-latex-placement="ht">
<figure>
<img src="figures/pop-up.PNG" />
<figcaption>Pop-up: Battery temp &gt; 89°C.</figcaption>
</figure>
<figure id="fig:alarm_icons2">
<img src="figures/alarm_icons.png" />
<figcaption>Alarm icons (2,3,4 and 5).</figcaption>
</figure>
<figcaption>Alarm icons (2,3,4 and 5).</figcaption>
</figure>

The next field is the binary **SEND MQTT** flag: if enabled, ToM+ published a MQTT message on the configured MQTT out topic (e.g. TOMout, see Section [4.2.4](#sec:mqtt_connection){reference-type="ref" reference="sec:mqtt_connection"}) when the alarm triggers as an additional notify. Last but not least is the **AUX CMD** text field, that holds an additional command to be sent via MQTT to other IoT devices. See the Appendix [7](#apx:tasmota){reference-type="ref" reference="apx:tasmota"} for detailed configurations of a Tasmota switch as an example.\
Finally you can add your alarm by pressing the **"Add to list"** button. The page automatically reloads and the alarm trigger is appended to the list in the first table.

Press the **"HOME"** green button at the end of the page to return to the landing page.

### Alarms log page {#sec:web_alarms_log}

This page stores the last 21 alarm triggers and does the same function as the log page of ToM, as shown in Section [3.5](#sec:alarm_log){reference-type="ref" reference="sec:alarm_log"}. You can see and remove any unwanted records as well, by pressing the **"Remove"** button near the one you would like to permanently delete (on ToM+ display too).\

<figure data-latex-placement="H">
<img src="figures/alarm_log1.png" style="width:60.0%" />
<figcaption>Alarm log page table.</figcaption>
</figure>

Obviously the table holds the **ITEM** and **VALUE** that triggered the alarm. But there are additional fields with the date and time when the trigger happened. Then, as usual, press the **"HOME"** green button at the end of the page to return to the landing page.

### OTA Update & Preferences page {#sec:web_ota_update}

In this page you can **update the firmware** on the fly from the web interface, without having to struggle with the flash tool as in the older versions. This new feature is time saving and much more user friendly, so be sure to have always the latest version of the firmware installed, to have access to the newest features and improvements!

#### OTA Update

The first table gives you some information about the blackbox firmware: let's discuss these values. The **ESP fw** is probably the most important item in the grid because it tells you the version that is currently installed and loaded on the ESP motherboard.

Another useful field is the **S/N** that stands for Serial Number, that you can find on ToM+ as well as we seen in Figure [3.3](#fig:settings_page){reference-type="ref" reference="fig:settings_page"}. The next row is a little more technical and it is strictly related to the OTA (Over-The-Air) update mechanism. **Current ptn** and **Next ptn** refer to the partitions addresses where the firmware is currently stored and where it will be stored while the update is in progress.\
Sometimes firmware patches, like bug fixes or minor stuff, may be released without changing the version number (e.g. 2.4). In these cases, it can be useful knowing which specific binary file is installed, so the next two fields hold its complete name. As you can see, there are two main firmware partitions, **Ota0** and **Ota1**, so that you can have two different versions installed and change between them if needed. Here, the full name is *ESP32_Fw24_70_4error12* for both.

The last field is the complete name of the **Special partition** firmware, which is an additional storage used to hold third-party softwares (e.g. the Twizy-cfg tuning software). For more information about tuning your Twizy using Twizy-cfg on ToM+ refer to Appendix [6](#apx:tuning){reference-type="ref" reference="apx:tuning"}.

<figure data-latex-placement="H">
<img src="figures/ota_page3.png" style="width:100.0%" />
<figcaption>OTA Update page — Update and info table.</figcaption>
</figure>

The second part of this table allows you to update the firmware or load a third-party software. First of all download the binary file (with the .bin extension) you want to install on ToM+. Then press the **"Browse..."** button and navigate your device folders until you find the desired file.

If it is a *standard ToM+ update*, go and press the **"UPDATE"** button. To check the update status, an orange progress bar will appear at the bottom of the table with its percentage. When it reaches 100% ToM+ will eventually reboot to apply the changes.

If it is a *third-party software*, be sure to check the *"Update to special partition"* option and, only after that, press the **"UPDATE"** button. As soon as the update is completed ToM+ will reboot and load the special partition firmware.\
In the **"BOOT OPTIONS"** table instead, once you have loaded the desired firmwares, you can switch bewteen them if needed. Let's say I'm running ToM+ 2.4 firmware and I want to do some tuning with Twizy-cfg third-party software; I have already loaded both of them in the correct partitions. In order to achieve this, press the *"Reboot from special partition"* button and wait for ToM+ to reboot, then follow the Appendix [6](#apx:tuning){reference-type="ref" reference="apx:tuning"} for more.\
*"Reboot from Ota0 partition"* and *"Reboot from Ota1 partition"* buttons are used to change between ToM+ firmware version. Let's say I'm running ToM+ 2.4 firmware but for some reason I want to get back to the 2.3 version I had before. To do so, press the respective button to reboot from either Ota1 and Ota0. ToM+ will instantly reboot and you will get disconnected to the web interface.

<figure data-latex-placement="H">
<img src="figures/ota_boot.png" style="width:100.0%" />
<figcaption>OTA Update page — Boot options table.</figcaption>
</figure>

Moving to the next one, we have the **"LCD FIRMWARE UPDATE"** table, that allows to perform OTA updates for the LCD display as well. This means no more struggling with the microSD card and the little hole on the display.\
**WARNING:** As written in the table you **MUST NOT** close this web page while updating: disabling your screen saver is adviceable to avoid update failure. The process may take some minutes, depending on the firmware version, up to 10 minutes.\
This is similar to the blackbox OTA update. So, first of all download the file (with the .tft extension) you want to install on ToM+. Then press the **"Browse..."** button and navigate your device folders until you find the desired file.

If you are *updating the main display*, go and press the **"UPDATE LCD"** button. To check the update status, the blue progress bar under the disclaimer box will show chunks copied to the LCD. When it finishes the display will reboot (not the blackbox).

If you are *updating the twin display*, be sure to check the *"Update AUX LCD"* option and, only after that, press the **"UPDATE LCD"** button. As soon as the update is completed the LCD display will reboot and load the desired firmware.

<figure data-latex-placement="H">
<img src="figures/ota_lcd.png" style="width:100.0%" />
<figcaption>OTA Update page — LCD firmware update table.</figcaption>
</figure>

#### Preferences and HW Upgrade

In the next web page section we can manage preferences, which includes WiFi and MQTT configurations, ToM+ pages icon arrangements and even more. So, it is always adviceable to have a **backup before updating**, to avoid entering your passwords again if an update goes wrong. In order to do that, press the **"BACKUP"** button and a file called *prefs.ToM* will be downloaded on your device. Sometimes a pop-up opens to warn you that this file has a strange extension, hit the *Keep* button and download it anyway.\
The opposite process is easy as well. Press the **"Browse..."** button and navigate your device folders until you find the preferences file *prefs.ToM*. To apply the changes press the **"RESTORE"** button and you will be redirected to the landing page as a confirm.

<figure data-latex-placement="H">
<img src="figures/prefs_page.png" style="width:100.0%" />
<figcaption>OTA Update page — Preferences backup table.</figcaption>
</figure>

This next table is very specific to users of older ToM versions that have now received the password to upgrade their device to ToM+ without changing the black box. If this is your case, please type the password in the text field and press the **"UPGRADE"** button. From now on, your ToM is finally upgraded to ToM+, enjoy!

<figure data-latex-placement="H">
<img src="figures/hw_upgrade.png" style="width:100.0%" />
<figcaption>OTA Update page — Upgrade hardware table.</figcaption>
</figure>

Press the **"HOME"** green button at the end of the table to return to the landing page.

### Advanced Info & Settings page {#sec:web_advanced_info}

This page is made for various advanced settings that aren't available in the ToM+ display settings pages discussed in Section [3.10](#sec:settings_page){reference-type="ref" reference="sec:settings_page"} due to space reasons.\
The first flag, **"Disable Auto-dimming"**, can be checked if you don't like ToM+ LCD display to adapt the brightness when turning on the light beams. Otherwise, you can adjust the **"Dimming brightness (%)"** expressed in percentage (up to 100%), and set by yourself the factor of brightness reduction when the light beams are activated.

<figure data-latex-placement="H">
<img src="figures/adv_sett_page1.png" style="width:100.0%" />
<figcaption>Advanced Info page — Advanced settings table.</figcaption>
</figure>

Next, we have the **Warning messages at power-off** subsection, where you can select the reminders (*light beam* and *handbrake*) and info (*system errors* and *charge limits*) shown on ToM+ shutdown pop-up. It looks like the one shown in the image below, letting you know, for instance, if you forgot to engage the handbrake. The last two check boxes are for future uses, not implemented yet.

<figure data-latex-placement="H">
<img src="figures/pop-up_finale.png" style="width:50.0%" />
<figcaption>Warning message at power-off.</figcaption>
</figure>

Then, there is the **"Secondary font colour"** with a color picker, used to change the secondary font colour on ToM+ display.

Another available flag is **"Invert current value sign"**. If checked, it basically shows a signed integer in current consumption values instead of their absolute values.\
The little subgroup below is dedicated to the **Cheatzy** compatibility with ToM+. You can set your **"Cheating factor"** multiplied by 10: for example, 2.0 becomes 20. You can also select if the Cheatzy is enabled when charging or during regenerative braking using the **"Cheat also Charge/Reku"** flag. These settings only make sense if the Cheatzy is connected and on, otherwise they may alter your current values incorrectly.\
Then, there is another flag: **"Increase thermal protection threshold"**, used to increase by 15°C the overheat safety threshold for ToM+ in warmer seasons.

The next two values are additional configurations for the ToM+ calculated **Remaining KM**, based on recent consumption sampling. Here you can adjust how often the sampling occurs (default: one per minute) in the **"Remaining KM sampling time (min)"** and how much the last sample affects the total calculation (default: 10%) in the **"Remaining KM sample weight (%)"**.\
Lastly we have the **"Miles to Kilometers"** flag, that helps when your BigToM was made from a mile-based dashboard, but you want km/h as its measure unit. If enabled, ToM+ will perform this conversion for you.

Please remember to **save your changes** by pressing the **"SAVE"** button at the end of this table. If you don't do this, your changes will be lost when you leave the page.

<figure data-latex-placement="H">
<img src="figures/adv_info.png" style="width:90.0%" />
<figcaption>Advanced Info page — Advanced info table.</figcaption>
</figure>

The table above holds data about your battery, such as stored capacity, **SOH**, **battery mileage**, total consumed kWh and about charges, such as the number of *total*, *full* and *partial* ones and the **maximum accepted charge power**.\

<figure data-latex-placement="H">
<img src="figures/item_scroll.png" style="width:100.0%" />
<figcaption>Advanced Info page — Items scroll table.</figcaption>
</figure>

This last table is a really peculiar feature introduced some updates ago that allows you to have dynamically changing items in pages of your choice. It can be applied to *battery*, *motor*, *gyroscope*, *trip* and *charging* pages and you can choose which one using the **"Page"** field.

Then, you can select which position you would like to be scrolling the data items of your choice. To do so, use the **"Position"** field and choose from the list the one you prefer, referring to Figure [3.4](#fig:icon_arrangement){reference-type="ref" reference="fig:icon_arrangement"} for the layout arrangement.\
The **"Freq"** field is the scroll frequency, basically how much time each data will stay in that position before ciclying to the next one. As you may notice, it is specified in brackets that the field will be multiplied by *5 seconds*. This means inserting the value *1* will result in a *5 seconds* frequency, the value *2* will result in a *10 seconds* one and so on.

The most important part is choosing the items to scroll and you can select up to ten data values. In the **"Scrolling items"** text areas, insert the list of desired item numbers (e.g. 59 or 48), one per each, referring to the numbers in brackets in the list of Section [3.1.2](#sec:item_numbers){reference-type="ref" reference="sec:item_numbers"}.\
Always remember to save your changes by pressing the **"SAVE"** button at the end of this table. If you don't do this, your changes will be lost when you leave the page.

If you want to **disable** the scroll feature for a specific page and position, select these fields and then input *0* in the **"Freq"** text box. Right after, press **"SAVE"** and the scroll will disable, returning to the default values.

Press the **"HOME"** green button at the end of the table to return to the landing page.

### Charging Preferences & Log {#sec:web_charging_prefs}

This page is split into two main tables: the first one is used to control the charging process, while the second one holds a list of the last 15 charging with some additional data.

#### Charging preferences

Starting from the most useful ones, we have a **"Charging status"** field that holds information about the current status of the car, including *220V main* and *charging process* with their ON and OFF flags.

Just below there is the **"Charge power limit"** box, where you can choose how much power your Twizy can use while charging, ranging from $0.4 kW$ up to $2.3 kW$ with 7 levels to choose from (select *0 to disable the power limit*).

In the top right corner there is the **"ABORT CHARGING"** button, that instantly stops gracefully the charging process, just like the one on ToM+ display in the settings page we discusses in Section [3.10](#sec:settings_page){reference-type="ref" reference="sec:settings_page"}.

<figure data-latex-placement="H">
<img src="figures/charging_process.png" style="width:100.0%" />
<figcaption>Charging Preferences page — Charging process control table.</figcaption>
</figure>

Right after there is the **"Stop charge at SOC %"** field, that is the charge percentage at which ToM+ automatically sends the signal to abort the charging process. Just for you to know, limiting the maximum charge range (95% or less) will slow down battery SOH decay.

Moving on to the next field, we have the **"Full charge after"** field that is strictly related to the last one we discussed. Basically, this won't stop charge at the selected SOC once every *X* charges (*for instance 10* as in the image). Bear in mind that a 100% charge once in a while is helpful to rebalance battery cells voltages.

Another related field is the **"Max charge once (next/current)"** flag, that works like a button and tells ToM+ to perform a full charge, without chosen SOC stopping. This overrides the previous field and will be applied, **after pressing "SAVE"**, to the current charging process if it is already in progress or to the next one if not.\
Now there is a safety field, the **"Charger max temperature"**, where you can set a threshold (integer value expressed in °C), that if passed with an user-defined margin hysteresis, ToM+ slowly reduces the power limit level we saw before. It keeps reducing it, by two levels if needed, until the temperatures returns normal and so will do the power limit.

The aforesaid margin is customizable in the appropriate **"Temp margin"** field, where you can input an integer value (expressed in °C), which will be added to the maximum charger temperature to loose the threshold before reducing charging power.

Another related field is the **"Abort temperature"**, that holds the last safety threshold for the charger temperature, that if passed makes ToM+ abort the charge immediately.\
Next we have three MQTT control fields, distinguished by their progressive number. By checking one of this flag allows you to configure remotely the parameter on its left using the MQTT protocol. To achieve this, after enabling the appropriate field and **pressing "SAVE"**, you will just need to publish a MQTT message on the topic specified between the brackets (e.g. *001* or *002*) on your broker (configured in Section [4.2.4](#sec:mqtt_connection){reference-type="ref" reference="sec:mqtt_connection"}).

If you enable the **MQTT control (001)**, you can start and stop the charging publishing either *0* or *1* on the MQTT topic *001*. Same is for **MQTT control (002)** publishing on *002* a value between *0* and *7* and **MQTT control (003)** on *003* with a value between *0* and *100*.\
Last but not least, we have the **"Aux Cmd"** field, that stands for auxilliary command, and behaves like the one we already discussed in the alarm trigger page in Section [4.4.8](#sec:web_alarm_triggers){reference-type="ref" reference="sec:web_alarm_triggers"}. It is sent when the charging is complete or when the charge stops at the specified SOC.\
After any change, press the **"SAVE"** button to *save your changes*, otherwise they will be lost when you leave the page.

#### Charging history

The charging history table holds the last fifteen charging processes along with some useful values to enrich them. As you can see, there is the date and time, along with the **ODO Kilometers** value when the charging started. Next to it, we have how much time the charging took and the **Average Power**, along with the **charged kWh**. Finally we have the *init SOC* and *end SOC*, that are the starting and ending percentage.\
The last column holds some additional **Notes** about the charging status, such as how did it stop (either stop SOC reached or manual aborted) or if it's still going.

If you want you can manually delete some records too, pressing the *X* button at the end of the desired record. It is possible to delete all of them at once by pressing the **"CLEAR HISTORY"** button located in the bottom part of the table.

<figure data-latex-placement="H">
<img src="figures/charging_history.png" style="width:95.0%" />
<figcaption>Charging Preferences page — Charging history table.</figcaption>
</figure>

Press the **"HOME"** green button below the last table to return to the landing page.

### Time & Date page {#sec:web_time_date}

With your ToM+ you can check the current date and time, but how to set it? This page was made for this exact purpose, and holds a single table shown in the image below.

<figure data-latex-placement="H">
<img src="figures/time_page.png" style="width:100.0%" />
<figcaption>Current Time &amp; Date table.</figcaption>
</figure>

The first five fields are self-explanatory and intuitive, just adjust date and time as in your timezone. The **"DST"** checkbox, that stands for Daylight Saving Time, allows you to enable or disable the 1-hour offset depending on current season.

When you want to confirm your changes and apply them to ToM+ just press the **"SET"** button and they will be updated.\
Next we have a very useful field, the **"Synchronize clock with WiFi"** flag, useful when you have some WiFi connection already configured as discussed in Section [4.1.2](#sec:add_wifi_profile){reference-type="ref" reference="sec:add_wifi_profile"}. Just turn this on and leave ToM+ making the hard work.

Just below there is a more technical value about the date-time that tells ToM+ what's your current time zone (**TZ**) using a string called **"POSIX"**. This includes when the DST 1-hour offset is applied. In most of center European countries the string is the following one: *CET-1CEST,M3.5.0/2,M10.5.0/3*, search online for your country POSIX TZ string if unsure.\
As always, remember to save your changes pressing the **"SAVE"** button at the end of the table, otherwise they will be lost when you leave the page.

Press the **"HOME"** green button below the table to return to the landing page.

### BigToM / ToM+ Settings page {#sec:web_btom_tom_sets}

In this page you can customize some parameters of you BigToM or ToM+, because this page mainly holds configurations for the **dashboard page**, available only in these two devices.

<figure data-latex-placement="H">
<img src="figures/btom_page.png" style="width:100.0%" />
<figcaption>BigToM \ToM+ Settings table.</figcaption>
</figure>

When replacing your dashboard with a BigToM one, you may have to add or substract some kilometers to the new dashboard ODO to have your original one. That's because they are stored in the dashboard motherboard. So, the first parameter is the **"ODO kms offset"** field, used to fix this kilometers difference.

As you may know, dashboard speed indicators are incresed by $3 km/h$ on purpose for safety reasons. If you want to see your real speed, just enable the **"Real speed (not ODO)"** flag in the second row of the table.\
Now let's have a look at the **"Lock touch while driving"** flag. If active, the touchscreen will be disabled while driving (i.e. speed $>0$) for safety reasons.

Next, we have the **Skip welcome animation** flag, that can be enabled if you are bored of seeing the welcome animation when changing from the dashboard to another page.\
Then, there is a section dedicated to the power bar shown in Figure [3.1](#fig:dashboard_layout){reference-type="ref" reference="fig:dashboard_layout"} at the top of the dashboard layout. Here you can choose, using the **"Power bar item"** choice box, what value should be shown and used to fill the power bar. There are three available data you can use: *Engine Torque*, *Battery Ampere* or *Battery kW*.

The two **"Up/Down section scale %"** fields below are used to adjust the range of the power bar and represent the percentage of the maximum/minimum value of the selected data item. In the example image, for the maximum range I put *30%*.\
In the next section we can enable another cool feature, shown in Figure [3.1](#fig:dashboard_layout){reference-type="ref" reference="fig:dashboard_layout"} as well, right below the speed indicator. This is achieved activating the **"Enable alert speed bar"** flag, that has three customizable thresholds, each one corresponding to a color from *green* to *yellow* and *red*.

The following three fields, **"Speed alert low/medium/high limit"**, are meant to be filled with the respective threshold speed in $km/h$ to light up the speed bar with the appropriate colour. In the example, the bar will become yellow when passing $50 km/h$ and then red when passing $70 km/h$. As you may notice, I didn't want the green bar to show up, so I put the *low* threshold value the same as the *medium* one.\
Last but one, we have the **"3D layout for charging page"** flag, enabled by default, that shows 3D details instead of the standard ToM charging page.

And finally there is the most recently added feature, called the **Twin ToM** and designed for the original ToM owners, before ToM+ came out. This allows you to use the smaller display along with the new clip-on version, in order to monitor two pages simultaneously. But to make this work you need to enable the last row flag, the **"Enable auxiliary display"** one.

Then you can select, with the **"Start page"** choice box, a specific page to show on the auxillary display at power on, or simply choose *Last shown*.\
As always, remember to save your changes pressing the **"SAVE"** button at the end of the table, otherwise they will be lost when you leave the page.

Press the **"HOME"** green button below the table to return to the landing page.

### Diagnostic page {#sec:web_diagnostic}

This page is composed by one table only and allows you to view more information about the last 10 errors that occured in your Twizy, similar to the ToM+ display page discussed in Section [3.8](#sec:error_page){reference-type="ref" reference="sec:error_page"}.

The shown values are the **"DTC Number"** and, if available, the **"DF Number"** that are unique identifiers for Twizy errors, so that you can search online for it. Next we have the error **"Status"**, such as *SAVED* if already happened or *PRESENT*, if it has just occurred.

To *enable DF Numbers*, please refer to Section [4.1.2](#sec:add_wifi_profile){reference-type="ref" reference="sec:add_wifi_profile"}.

<figure data-latex-placement="H">
<img src="figures/error_page.png" style="width:100.0%" />
<figcaption>Diagnostic page — Error list table.</figcaption>
</figure>

Along with these values, the next four values are the reference **"ODO"**, **"SOC"**, **"speed"** and **"12V Battery voltage"** when the corresponding error occured.

For each error record, if available, there is an error **"Description"** field.\
If you would like to clear Twizy errors, even fatal ones, you can press the below **"DELETE ERRORS"** button, that will delete all of them at once.

Press the **"HOME"** green button below the table to return to the landing page.

# How to update your ToM+ firmware {#sec:update_procedure}

## Requirements before updating

ToM+ is constantly evolving, since quite every day I receive suggestions to improve some features or even adding some cool ones. I'm trying to consider all pieces of advice from each owner and these tips and ideas will result in firmware updates. While testing the device on drive, if you notice bugs or weird stuff please report them to me and they will result in firmware patches. As I said at the beginning, ToM+ is constantly improving, so stay tuned...

### Why should I update?

Well, new update means new features and bug fixes, so why should you keep the old firmware version when you can easily install the latest stable one? So, there's no reason to keep your ToM+ outdated, since upgrading its software is **free forever** and gives you a lot of satisfaction and fun while trying out new features. In the end, I personally advice you to keep your ToM+ updated and safer.\
Anyway all older firmware versions are still available on the Twizy forum in ToM section (<https://www.twizy-forum.de/twiz-o-meter>) under *"\[Twiz o'meter\] Update to firmware x.x"* topics. In fact, ToM+ allows downgrades too, if needed.

### What do I need to update?

In the next sections will be discussed an alternative way to update, much more time consuming compared to the OTA method already discussed in Section [4.4.10](#sec:web_ota_update){reference-type="ref" reference="sec:web_ota_update"}. I personally **suggest the OTA method**, because it's safer and easier to do if you're not really into IT and embedded systems.\
If you're still convinced to upgrade ToM+ firmware with the second method, there are a couple of things you will need in order to complete the update successfully. First of all, you will need a computer and both desktops or laptops are great for this work.

Later we will see how to connect ToM+ to our computer in order to transfer the new upgrade files on it. The second thing you must get is a micro USB cable, which is the same that is usually used in rechargeable device and older smartphones. You will also need a microSD card with a storage capacity between 8 and 32 GB. Examples are shown in the photos down below. And of course you will need your ToM+!

<figure data-latex-placement="H">
<img src="figures/cables_sd_update.png" style="width:80.0%" />
<figcaption>microUSB cables and example microSD card.</figcaption>
</figure>

### How do the update files look like? {#sec:update_files}

Before you update the firmware, you obviously need to download from the Twizy forum (again <https://www.twizy-forum.de/twiz-o-meter>) the desired version update ZIP. You will probably need to register to the forum to see and download firmware files and images. It's a really cool and active community, so I suggest to become a member anyway. After extracting the files in the folder, this is what you should get:

<figure data-latex-placement="H">
<img src="figures/firmware_release_folder.png" style="width:100.0%" />
<figcaption>Firmware release folder files list.</figcaption>
</figure>

First of all, we notice a text file with the *changeLog23.txt*, used to track the added features and bug fixed in the latest firmware release. Read it if you are curious to know what's new or if you need additional help with the update procedure.\
Next, there are two folders containing the **LCD display firmware** update in a *.tft* format. **Choose the version** made for your device: first folder if you got a ToM+ or a BigToM (that means bigger display) or the other one if you have a traditional ToM or you're willing to update the Twin ToM (smaller screen). This is a crucial step, otherwise new icons and graphics won't fit your display size.\
The last one is the *ESP32Fw23.bin* binary file for the **black box update**. Make sure to have all of these files, because you will need them in the next steps.

### What should I know before update?

Now let's prepare our ToM+ to be updated by **toggling OFF the switch** on the black box. Make sure to switch it off (*i.e. 0 symbol on the switch*) or you will surely cause serious problems to ToM+.

So, if your Twizy is still powered on with the key in, simply switch it completely off and remove the ignition key. After this easy steps, you are ready to get into the update procedure, but remember to strictly follow the steps discussed in the guide. Don't proceed by intuition, otherwise you will risk to permanently brick your device.\
The upgrading process is quite easy and you will need to update both the LCD firmware and the black box one, in this specific order. We will see how in the next section.

## Updating LCD firmware

The LCD display is one of the essential parts of ToM+ as it was discussed in the first two chapters and for this reason it will need to be updated as well. New firmware means new icons and different layouts and, in order to upload the new ones onto it, it's crucial to use a small **microSD card** to accomplish this task. ToM+ SD card slot is under the display so you may need to temporarily remove it from your glove box so that you can better work on it, or simply tilt it backwards and you will see the hole.

### Preparing the microSD card

Unfortunately, not all microSD cards are working with the display, especially newer ones made for cameras, but for now I have tried class 10 HC 8 to 32 GB ones and they seem to work well. But feel free to try with your own memory card and see if it works.\
Now that we've chosen a microSD card, that must have a storage capacity **between 8 and 32 GB**, we need to copy the LCD firmware on it. Before copying the file on it, we must make sure that there aren't any other files or the upgrade won't work.

So, move any files to your computer and format the microSD card in a **FAT32 format** as I did in the screenshot here. To achieve that right, click on the card icon in your file explorer and select the **"Format"** option from the dropdown menu.

<figure data-latex-placement="H">
<img src="figures/forma_sd_steps.png" style="width:70.0%" />
<figcaption>How to FAT32 format microSD steps.</figcaption>
</figure>

As it's shown in the picture, select **FAT32** file system, then check the **"Quick Format"** option and press the **"Start"** button to begin the process. Wait until it's finished and then copy the *.tft* file attached in the firmware release you want to install, contained in the update ZIP folder.

### Inserting the microSD card

Now, we are ready to put the microSD card in the LCD display slot. It may help using some snipe nose pliers to carefully insert the microSD card. This should ensure you would center the internal SD card slot.\
**REMEMBER!** The microSD card fits in the slot only in one way, with the contacts side pointing to the screen surface, as shown in the image. If it doesn't, don't force it! Try turning it to the other side.

Now that the microSD card is inserted in the internal slot, slowly push it into the box until your hear a "click" sound. This will mean that you can safely remove the pliers without losing the card inside the box.

<figure data-latex-placement="H">
<img src="figures/sd_insert.jpg" style="width:60.0%" />
<figcaption>Insert the microSD in the display hole.</figcaption>
</figure>

### The updating workflow

Once the microSD is in, we can carry on with the updating workflow. Now, let's get back to our Twizy and plug the display back to the black box. Then, power on the display using the switch on the black box (*i.e. 1 symbol on the switch*) and, only after that, power on your Twizy using the ignition key.

Wait for the LCD display to start the updating process until you see the progress percentage as shown in the figure below (both for the ToM+ and ToM display). The microSD copying process will usually take up to a minute and a half.

<figure data-latex-placement="ht">
<figure>
<img src="figures/update_screen_lcd.jpg" />
<figcaption>ToM+ display update.</figcaption>
</figure>
<figure>
<img src="figures/copy_sd_card.png" />
<figcaption>ToM display update.</figcaption>
</figure>
<figcaption>ToM display update.</figcaption>
</figure>

Once the updating of the LCD firmware is completed successfully you will see this screen, saying that the **"Update Succeeded!"**. After update, **DON'T** power on with the microSD inserted! Now, we can power off the car and the switch OFF ToM+ again using the switch on the black box.

Then, remove the microSD card while the whole system is powered off and the LCD update is complete. **REMEMBER!** If you remove the card with ToM+ powered on you will permanently brick the device! After that, without changing the state of the overall system let's proceed with the black box update, as shown in the next section.

## Updating black box firmware (Windows)

The black box is the second essential component of ToM+ and it's the brain of the whole system. If we update the display only, then the black box won't know what those new icons are intended for and this will cause mismatches in the communication.

So it's crucial to mount the new firmware on the motherboard of ToM+ as well. To do that, we won't need the microSD card anymore, but we will use the microUSB cable we prepared before and the computer. In fact, we will flash the firmware directly on the ESP32 board to mount the new software.

### Preparing the computer

Before plugging the cable in the computer, we need to install some programs to let it work properly. The **ESP32 board** needs some drivers to be recognized by the operative system, so we will download them directly from the official website.

From the download page of the [Silicon Lab website](https://www.silabs.com/software-and-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads), we need to choose our operative system version, as we can see in the screenshot I've taken down here.

<figure data-latex-placement="H">
<img src="figures/driver_download.png" style="width:100.0%" />
<figcaption>Driver dowload page on Silicon Lab.</figcaption>
</figure>

Since this section of the guide is specific to any Windows operative system we will download the *"CP210x Windows Drivers"* package pressing on the link pointed in yellow in the image above.

The downloaded file will be a ZIP folder, usually called *"CP210xWindowsDrivers.zip"* in which you can find a couple of folders and some files. In the screenshot below are listed all the usual files contained in the ZIP folder.

<figure data-latex-placement="H">
<img src="figures/driver_folder.png" style="width:70.0%" />
<figcaption>Contents of driver ZIP folder.</figcaption>
</figure>

Extract all the files in a dummy folder in your Desktop. Now, it's important to choose the right *".exe"* file to run in order to install the drivers. If your operating system is 64 bit (for most computers) you will run *CP210xVCPInstallerx64.exe* file, otherwise the second *".exe"* file is the properly one, as show in the image.

Make sure to run the executable file with admin permission by right clicking on it and selecting **"Run as Administrator"** option. If prompted allow the program to perform admin operations on your computer, or the driver installation process won't start.

<figure data-latex-placement="ht">
<figure>
<img src="figures/wizard_step1.png" />
<figcaption>First step: Press “Next”.</figcaption>
</figure>
<figure>
<img src="figures/wizard_step2.png" />
<figcaption>Second step: “Accept” and “Next”.</figcaption>
</figure>
<figcaption>Second step: “Accept” and “Next”.</figcaption>
</figure>

Once the installer starts you will see a window like the one shown on the left. This is a wizard tool to install the drivers you will need to recognize the black box from your computer. Now let's press the **"Next"** button as shown here to start the whole process.\
The next window you will probably see is this one shown on the right. Here you must accept the license by checking the first button **"Accept the license"**. Then, you can press the **"Next"** button as shown here and start the copy of the drivers in the right system folder: wait for the copy to finish.

When the copy is done, the installation of CP210X drivers is complete and you can safely plug in the black box into your computer. Now press the **"Finish"** button to close the window.\
Before doing anything make sure that the switch on ToM+ black box is powered OFF (*i.e. 0 symbol on the switch*). The Twizy must be powered off as well because, if you try plugging the cable in your PC while ToM+ is still powered by the car, you will mix power supplies (5V and 12V) and ToM+ will definitely die.

<figure id="fig:black_box_labels" data-latex-placement="H">
<img src="figures/black_box.jpg" style="width:60.0%" />
<figcaption>The black box components.</figcaption>
</figure>

The black box has a small microUSB connector on the rear side, as you can see in the image above. So, connect the microUSB cable side and to the black box. After that, connect the USB side of the cable to a free USB port on your computer.

**REMEMBER!** Both sides of the cable fits only in one way in the corresponding plugs, so don't force them or you will risk to brake the ToM+ port or your computer one. Try turning it to the other side and check if it works that way.\
Now the computer should recognize the black box ESP32 board, if you installed the drivers properly. To check if it's so, search for the **"Device Manager"** app on your PC and run it.

Now you should have opened a window that looks like the one shown in the figure down below. Find the **"Ports"** row with a connector icon and double click it, opening the list of all of your serial devices. As I did in the screenshot look for *"Silicon Labs CP210x to UART Bridge (COMx)"* and then note down the COM number, that is **COM8** in the example. This number will be useful in the next step to tell the PC where to upload the new firmware version. Let's continue this process...

<figure data-latex-placement="H">
<img src="figures/device_manager.png" style="width:80.0%" />
<figcaption>Device manager UART serial port (COM8).</figcaption>
</figure>

Visit the [ESP32 official website](https://www.espressif.com/en/support/download/other-tools) to download a tool that we will need to flash the firmware on our black box board. Look for **"Flash Download Tools"** and press the button as shown in the image. Then, search in the page for the *"Flash Download Tools"* with the save icon and press it.

It will download a ZIP folder called *"flashdownloadtoolx.x.x.zip"*, where the "x" symbols will be replaced by the version name, which is **V3.9.11** in this example. Opening the downloaded ZIP folder, you will notice that there is another folder in it. Extract that one on your Destktop or wherever you want and open it. The files contained in it would usually be the ones listed in the screenshot below.

<figure data-latex-placement="H">
<img src="figures/esptool_folder.png" style="width:70.0%" />
<figcaption>Contents of Flash Tools ZIP folder.</figcaption>
</figure>

Select the *"flashdownloadtool.11.exe"* or whatever version you downloaded and run it with admin permissions, by right clicking on the file and selecting **"Run as Administrator"** option. If prompted, allow the executable file to perform operations on your computer.\
Once the program is started, you should see a terminal window opening, that is going to lunch in some seconds the user interface. It should look like as the first one shown in the example here. You need to change the **"ChypType"** to *"ESP32"* as it's shown in the second step down below. Leave the rest as it is and press **"OK"** button.

<figure data-latex-placement="H">
<img src="figures/launching_flashtool.png" style="width:85.0%" />
<figcaption>Select ESP32 motherboard in the choice box.</figcaption>
</figure>

### The updating workflow

As soon as you press the **"OK"** button a *"ESP32 DOWNLOAD TOOL"* window will open. Now, extract the binary file (*.bin* extension) attached in the ToM+ firmware release ZIP as we discussed in Section [5.1.3](#sec:update_files){reference-type="ref" reference="sec:update_files"}.

Then, press the **"..."** button shown in the first image and select the path of the *".bin"* file. Once you did that, press the **"Open"** button and you will see a green record in the first line containing the path you've just confirmed.

Proceed by **flagging the check box** next to the first line, choosing the firmware you want to upload. Then, type in the text box shown in the second picture this sequence of characters: **0$\times$`<!-- -->`{=html}10000** (with four zeros). This represents the starting memory address where the firmware files will be stored.

Now, it comes the last step of the configuration: select the COM number using the list box in the bottom right corner. Make sure to select the right COM, which is the one we previously note down from the **Device Manager** page.

<figure data-latex-placement="H">
<img src="figures/flashtool_page.png" style="width:100.0%" />
<figcaption>ESP32 Download Tool configuration steps.</figcaption>
</figure>

Now let's start the update pressing the **"START"** button as shown in the first picture. A green progress bar will appear in the bottom of the window and the whole process should usually take a couple of minutes.

Once the upload is completed, you will see a **"FINISH"** message in the green box at the bottom left corner, as shown in the image. As an additional confirm, the progress bar will be full and now the update is done.

<figure data-latex-placement="H">
<img src="figures/flashtool_page2.png" style="width:100.0%" />
<figcaption>ESP32 Download Tool finalizing update.</figcaption>
</figure>

Now close this window and then you can safely unplug the cable from both your PC and ToM+. Only after this actions, you can restore the normal power supply of ToM+, moving the switch to the 1 state and powering on your Twizy using the ignition key.

To restore your previous configurations, enter in the ToM+ settings page by pressing the three dots in the top right corner and then press the exit button without doing anything. Doing that way you will update the data structure saved in black box memory and your configurations are back too.\
**Congratulations!** You've finished the whole updating process, now enjoy the new firmware and remember to report any bugs or problems to me through private messages, attaching an image perhaps.

## Updating the black box (Unix)

The black box is the second essential component of ToM+ and it's the brain of the whole system. If we update the display only, then the black box won't know what those new icons are intended for and this will cause mismatches in the communication.

So it's crucial to mount the new firmware on the motherboard of ToM+ as well. To do that, we won't need the microSD card anymore, but we will use the microUSB cable we prepared before and the computer. In fact, we will flash the firmware directly on the ESP32 board to mount the new software.

Before doing anything, turn OFF ToM+ black box switch (*i.e. 0 symbol on it*) and power off your Twizy as well. It's an important step to strictly follow to avoid damages to the device.

### Preparing the computer

Download the ToM+ firmware update folder attached to the firmware release post. Now, extract the binary file (*.bin* extension) attached in the ToM+ firmware release ZIP as we discussed in Section [5.1.3](#sec:update_files){reference-type="ref" reference="sec:update_files"}. The file in it is usually called *"FwXXESP32.bin"*, where the *"XX"* symbol will be replaced by the version number, for instance *"23"*.\
**Disclaimer:** *this black box process was tested using Ubuntu 20.04 (hope it will work with other Unix distribution too). Do not plug the black box until explicitly told to do so*.\
Now we need to install the esptool package, to flash the new firmware onto the black box. Do this, either with the package manager UI provided by your Unix distribution, or with the appropriate command in a terminal. For instance, *"sudo apt-get esptool"*, as shown in the image. If prompted, type in the password of the sudo user, then press ENTER and wait.

<figure data-latex-placement="H">
<img src="figures/apt_get_esptool.png" style="width:100.0%" />
<figcaption>Installing esptool package on Ubuntu.</figcaption>
</figure>

Next you need to install python, if you don't have it, since the esptool is written in python language. So you need to type the command *"sudo apt-get python"*, as shown in the image. Again, if prompted, type in the password of the sudo user, then press ENTER and wait.

<figure data-latex-placement="H">
<img src="figures/apt_get_python.png" style="width:100.0%" />
<figcaption>Installing python package on Ubuntu.</figcaption>
</figure>

Once we have installed both packages type *"sudo tail -f /var/log/messages"* in the terminal as shown in the image to monitor in real-time the log file, that will show us which COM the black box will be associated to by the OS. If prompted, type in the password of the sudo user, then press ENTER. **Now we can plug in the black box**.

<figure data-latex-placement="H">
<img src="figures/tail_com.png" style="width:100.0%" />
<figcaption>Monitor real-time COM connections.</figcaption>
</figure>

The black box has a small microUSB connector on the rear side, as you can see in Figure [5.1](#fig:black_box_labels){reference-type="ref" reference="fig:black_box_labels"}. So, connect the microUSB cable side and to the black box. After that, connect the USB side of the cable to a free USB port on your computer.

**REMEMBER!** Both sides of the cable fits only in one way in the corresponding plugs, so don't force them or you will risk to brake the ToM+ port or your computer one. Try turning it to the other side and check if it works that way.\
As soon as you plug the black box to the computer you should get an output similar to this one shown in the block of code down here.

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

The line we are interested in is this one: *"cp210x converter now attached to ttyUSB0"* where the word **"ttyUSB0"** is the serial port where the black box is attached. So, note down this port, that can be different from mine, because we will need it while uploading the new firmware.

### The updating workflow

Navigate with your file manager in the folder where the firmware *.bin* file is stored and open a terminal in it by right clicking on the folder and selecting **"Open Terminal"** option from the dropdown menu. Or if you prefer, you can manually navigate through your folders using the "cd" command until you find the right one.

Once you are in the correct directory, execute this long and boring command, replacing *"ttyUSBx"* with the serial port name we noted down in the step before (e.g. *"ttyUSB0"*) and *"ESP32FwXX.bin"* with the name of the *".bin"* file which contains the firmware version to load on ToM+ (e.g. *"ESP32Fw23.bin"*).

        python /usr/share/esptool/esptool.py --chip auto --port /dev/ttyUSBx --baud
    921600 --before default_reset --after hard_reset write_flash -z --flash_mode dio
    --flash_freq 40m --flash_size 4MB 0x10000 ESP32_FwXX.bin

You should receive an output similar to the following one:

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

Now close this window and all the others and then you can safely unplug the cable from both your PC and ToM+. Only after this actions, you can restore the normal power supply of ToM+, moving the switch to the 1 state and powering on your Twizy using the ignition key.

To restore your previous configurations, enter in the ToM+ settings page by pressing the three dots in the top right corner and then press the exit button without doing anything. Doing that way you will update the data structure saved in black box memory and your configurations are back too.\
**Congratulations!** You've finished the whole updating process, now enjoy the new firmware and remember to report any bugs or problems to me through private messages, attaching an image perhaps.

# Tuning on your ToM+ (Twizy-cfg) {#apx:tuning}

## What is Twizy-cfg?

[Twizy-Cfg](http://github.com/dexterbg/Twizy-Cfg) is an **open-source**, light-weight configuration shell designed for the SEVCON Gen4 motor controller embedded within the Renault Twizy, developed by [dexterbg](https://github.com/dexterbg). Developed to run on Arduino microcontrollers equipped with an MCP2515 SPI CAN-bus module, this tool provides hardware hackers, technicians, and EV enthusiasts with a direct command-line interface to interact with the vehicle's drive system via the standard **OBD-II diagnostic** port.\
At its core, Twizy-Cfg acts as a bridge between *high-level* macro commands and *low-level* CANopen SDO (Service Data Object) register operations. It enables precise tuning and monitoring of the powertrain, offering capabilities such as:\

- Drive Profile Customization: Adjusting key performance parameters, including maximum power, torque limits, top speed, and acceleration ramps.

- Energy Management: Fine-tuning energy recuperation levels during coasting and braking to balance driving range against braking force.

- Profile Management: Saving, loading, and restoring custom performance profiles directly to and from the Arduino's EEPROM.

- Diagnostics & Low-level Access: Issuing raw CANopen commands and basic OBD-II diagnostic requests to inspect controller states and firmware revisions.

 \
This appendix will cover how ToM+ can handle a special partition with the above mentioned piece of software, that have been adapted to work on its ESP32 board (ToM+ chip).

## Requirements before starting

**DISCLAIMER!** The target of this appendix is installing and running in the blackbox an alternative firmware, not coded by me, using the hardware for a different purpose than the one for which it was build. Following this guide, you'll have a **dual boot blackbox**, with ToM+ firmware and Twizy-cfg firmware living together, each bootable according to your need.\
To achieve this goal you will need a black box running a firmware version **1.45** or above. This is a crucial requirement, because this process needs the OTA update feature, that was introduced in the mentioned version. See Section [3.10](#sec:settings_page){reference-type="ref" reference="sec:settings_page"} to check your ESP firmware version and Section [4.4.10](#sec:web_ota_update){reference-type="ref" reference="sec:web_ota_update"} to update your firmware via OTA if needed.\
Then, you will need the compiled version of ESP32 compatible Twizy-cfg, that you can download from [this link](https://www.mediafire.com/file/n5waunl2w19cpl6/TwizyCfg_ok.ino.bin.zip/file). Extract its content and keep the *".bin"* file that we will need later.

## The updating workflow

Now connect to the web server following one of the methods exaplained in Section [4.4.2](#sec:web_server_access){reference-type="ref" reference="sec:web_server_access"} and then navigate through the **"OTA Update and Prefs"** page (Section [4.4.10](#sec:web_ota_update){reference-type="ref" reference="sec:web_ota_update"}) and use the previously extracted *".bin"* file to perform the update, selecting the **"Update to special partition"** flag (otherwise you will replace the original ToM+ firmware).\

<figure data-latex-placement="H">
<img src="figures/ota_page3.png" style="width:100.0%" />
<figcaption>OTA Update page — Update and info table.</figcaption>
</figure>

When the update progress bar reaches 100%, ToM+ LCD display will become black and that is the successful sign that ToM+ is rebooting, loading the *Twizy-cfg* software. Now, you need to connect to **"Twizy-cfg"** access point on your device to access its webserver and if requested, accept to keep the connection active even if it doesn't provide an Internet access.

The **password** is the default ToM+ password, which is the word "pass" followed by your device serial number (e.g. *pass129777*). Serial number can be found in the settings page as explained in Figure [3.3](#fig:settings_page){reference-type="ref" reference="fig:settings_page"}.\
Now, open a web browser and type **192.168.4.1/webserial** to navigate to the web server interface, where you can send tuning commands. The command terminal looks like the one shown in the image here. As already said, tuning isn't an official ToM+ feature and *Twizy-cfg* wasn't written by me, so please refer to [Twizy-cfg topic](https://www.twizy-forum.de/projekte-twizy/83451-twizy-cfg-sevcon-shell-fuer-arduino?start=0) or to its [Github repository](https://github.com/dexterbg/Twizy-Cfg) to know tuning commands and configurations.\

<figure data-latex-placement="H">
<img src="figures/TuningMonitor.PNG" style="width:70.0%" />
<figcaption>Tuning monitor to perform tuning commands.</figcaption>
</figure>

As long as you are using Twizy-cfg, ToM+ firmware won't be loaded and so the display won't power on. When you want to get back to official ToM+ firmware, you will just need to type in the tuning monitor this self-explanatory command: **reboot**.\
And that's it, ToM+ reboots to the other partition and gets back to its normal behaviour and the tuning configuration will persist in your Twizy. The next time you will need the Twizy-cfg shell, just go in the **"OTA Update and Prefs"** page on ToM+ web server and select the option *"REBOOT FROM SPECIAL PARTITION"* from the table shown in the next image. No need to upload the *".bin"* file again.

<figure data-latex-placement="H">
<img src="figures/ota_boot.png" style="width:100.0%" />
<figcaption>OTA Update page — Boot options table.</figcaption>
</figure>

# Controlling Tasmota WiFi switch {#apx:tasmota}

## What are WiFi switches/plugs?

In this appendix I'll explain how you can configure your ToM+ to interact with a WiFi AC switch / AC plug, or any other device running a **Tasmota firmware**.

Basicaly they are *relais modules* which can be controlled remotly via a wireless connection. You can easly find this sort of devices on lots of e-commerce websites (like Amazon), for a few tens of euros.\
They have many formats, but frequently they appear in the two shown in the image. The second one is more compact and user-friendly, while the first one needs some cable connection to work with your electric equipments.

<figure data-latex-placement="ht">
<figure>
<img src="figures/Sonoff.PNG" />
<figcaption>Sonoff WiFi smart switch.</figcaption>
</figure>
<figure>
<img src="figures/TasmotaPlug.PNG" />
<figcaption>Tasmota WiFi smart plug.</figcaption>
</figure>
<figcaption>Tasmota WiFi smart plug.</figcaption>
</figure>

*But why is this useful?* There are many reasons you could need ToM+ connected to these devices. Let's say: you want to stop traction battery charging if the charger is overheated and restart charging when the temperature decreases; or maybe you want to **stop charging** when a desired SOC is reached.

Or, like I did in this appendix with experimental purposes, to light on a lamp in my room when Twizy (parked in the garage) has almost completed charging. In short, there are plenty of useful ideas where a WiFi switch/plug along with ToM+ can help, creating nice projects.

## Requirements before starting

To achieve this goal you will need a black box running a firmware version **1.4** or above. This is a crucial requirement, because this process needs features that were introduced in the mentioned version. See Section [3.10](#sec:settings_page){reference-type="ref" reference="sec:settings_page"} to check your ESP firmware version and Section [4.4.10](#sec:web_ota_update){reference-type="ref" reference="sec:web_ota_update"} to update your firmware via OTA if needed.

Additionally, you will need to have **WiFi and MQTT configured** to make the whole system work. If not, please refer to Section [4.1](#sec:wifi_settings){reference-type="ref" reference="sec:wifi_settings"} to set up WiFi and to Section [4.2.4](#sec:mqtt_connection){reference-type="ref" reference="sec:mqtt_connection"} for the MQTT configuration. They must be both enabled and connected to accomplish this task.\
Then, you will obviously need a wireless switch or plug, depending on your needs and it must be running a **Tasmota firmware** (*version 7* or above).

Bear in mind that *"Sonoff"* like devices come out the fabric with a proprietary firmware which doesn't natively support MQTT protocol.\
In order to use them, as I did in this appendix, you have to upgrade them to Tasmota firmware. Web is full of guides about installing Tasmota firmware, so look for the one that suits your device and follow it. For users who don't want to face with firmware update procedure, I personally suggest to buy a device already running Tasmota firmware.

## Tasmota MQTT configuration

Navigate to the **Tasmota WebUI** and you will get a landing page similar to the one show below. At any time, if unsure, please refer to the [official documentation](https://tasmota.github.io/docs/).

<figure data-latex-placement="H">
<img src="figures/Mqtt1.PNG" style="width:45.0%" />
<figcaption>Tasmota webUI — Landing page.</figcaption>
</figure>

First of all, press the **"Configuration"** button that will take you to the page shown in the first image below. After that, configure the *WiFi connection*, entering your parameters (SSID and password) in Tasmota's **"Configure WiFi"** page. Then, follow the instruction to configure *MQTT settings*, accessing **"Configure MQTT"** webUI page.\

<figure data-latex-placement="ht">
<figure>
<img src="figures/Mqtt2.PNG" />
<figcaption>Configuration page.</figcaption>
</figure>
<figure>
<img src="figures/Mqtt4.PNG" />
<figcaption>MQTT configuration page.</figcaption>
</figure>
<figcaption>MQTT configuration page.</figcaption>
</figure>

Now enter your broker address, user ID, password and port number. They must be the same set on ToM+! You can check the explanation for each field in Section [4.2.4](#sec:mqtt_connection){reference-type="ref" reference="sec:mqtt_connection"}.\
The most difficult parameters to understand are **"Topic"** and **"Full Topic"**. These must not be the same as ToM+ MQTT topics, because they are specific for the device you are using. If you put the same *TOMin* and *TOMout* topics the communications may disturb each other.\
In the first field enter whatever you want. I suggest something that reminds your device function. But please use a short string (5/6 chars are enough), because this field will be a minimal part of the full topic string and ToM+ has a limit of 50 chars for **"Auxilliary MQTT command"** field (discussed in Section [4.4.8](#sec:web_alarm_triggers){reference-type="ref" reference="sec:web_alarm_triggers"}).

In the second field, it's important to distinguish between two options, depending on which broker you are using. If you have your own broker (i.e. *not Maqiatto*), then leave the default string **%prefix%/%topic%/**.\
If you use Maqiatto instead, configured following Section [4.2.3](#sec:free_broker){reference-type="ref" reference="sec:free_broker"} or any another broker which adds *your email as a prefix* of the topic name, then edit the **"Full Topic"** field accordingly. The fields will be the one shown in the second image above, so it becomes **myemail@gmail.com/%prefix%/%topic%/**, adding your userID (email) as a prefix.

Finally, press the **"Save"** green button and wait until the device reboots.\
**REMEMBER!** If you are using Maqiatto broker, you may need to add the new topic to your account as explained in Figure [4.2](#sec:free_broker_add_topics){reference-type="ref" reference="sec:free_broker_add_topics"}.

In this case, you'll have to add **cmnd/\<your Tasmota topic name\>/Power** as the new topic name, that will become *cmnd/charge/Power* if you followed the image.

## ToM+ Tasmota configuration

Open ToM+ webserver as explained in Section [4.4.2](#sec:web_server_access){reference-type="ref" reference="sec:web_server_access"} and go to the **"Alarm triggers"** page. Now, add a new allarm to the list accordingly to the item which will control your Tasmota device, as explained in Section [4.4.8](#sec:web_alarm_triggers){reference-type="ref" reference="sec:web_alarm_triggers"}.

In my case, I chose **"Battery SOC"** item, that will trigger alarm when its value will be *equal to 97%*, to notify the quite completed charge.

<figure data-latex-placement="H">
<img src="figures/Tom01.PNG" style="width:70.0%" />
<figcaption>Adding the Tasmota trigger on ToM+.</figcaption>
</figure>

As you may notice, the most important part is to configure properly the **"Aux Cmd"** field, because it contains the control MQTT command that ToM+ will send to the Tasmota device.

If you have your own MQTT broker (i.e. *not Maqiatto*) the **Aux Cmd** will have this syntax:

- *cmnd/\<your Tasmota topic name\>/Power 1* if you want to power ON the device.

- *cmnd/\<your Tasmota topic name\>/Power 0* if you want to power it OFF.

Again, in our example the command becomes **cmnd/charge/Power 1** to power the lamp ON.\
Otherwise, if you are using Maqiatto broker or another one which uses your userID (e-mail) as a prefix in topics name, then the **Aux Cmd** syntax will look in this other way:

- *myemail@gmail.com/cmnd/\<your Tasmota topic name\>/Power 1* to power it ON.

- *myemail@gmail.com/cmnd/\<your Tasmota topic name\>/Power 0* to power it OFF.

In our case, the command becomes **myemail@gmail.com/cmnd/charge/Power 1**.\
If you want to stop charging and then restart when specific conditions are met, you need to add two alarms, one for each Power ON/OFF condition, using the explained syntax accordingly.\
Please note that, if you have a device with more relais, you will have to edit the above syntax specifying which relais you want to control: using **"Power1"** for the first relay, **"Power2"** for the second one and so on. This becomes:

- *cmnd/\<your Tasmota topic name\>/Power1 1* to power ON the first relay.

- *cmnd/\<your Tasmota topic name\>/Power1 0* to power it OFF.

The same syntax distinction about Maqiatto and owned brokers applies here as well.

## Common problems and fixes

Some Tasmota firmwares don't like *Maqiatto* topic format, so if you want to drive a Tasmota device with ToM+, you have to use another MQTT broker. After some tests, I noticed you can use successfuly use [mqtt.dealgate.ru](https://dealgate.ru/), free and more features-rich.

The downside is that you have to face with some russian translations to create the account. But nothing than an online translator cannot do.
