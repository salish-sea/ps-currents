## Puget Sound Surface Currents

[Test link to hello.html](hello.html)
[Test link to docs dir](docs)

### LiveOcean's prediction for today:

|                                                                                                                 |                                                Pacfic time zone                                                 |                                                                                                                 |
|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------:| 
| [![LiveOcean surface currents](data/latest-LO/thumbs/plot_0014.png)](data/latest-LO/img/plot_0014.png)<br>06:00 | [![LiveOcean surface currents](data/latest-LO/thumbs/plot_0015.png)](data/latest-LO/img/plot_0015.png)<br>07:00 | [![LiveOcean surface currents](data/latest-LO/thumbs/plot_0016.png)](data/latest-LO/img/plot_0016.png)<br>08:00 |
| [![LiveOcean surface currents](data/latest-LO/thumbs/plot_0017.png)](data/latest-LO/img/plot_0017.png)<br>09:00 | [![LiveOcean surface currents](data/latest-LO/thumbs/plot_0018.png)](data/latest-LO/img/plot_0018.png)<br>10:00 | [![LiveOcean surface currents](data/latest-LO/thumbs/plot_0019.png)](data/latest-LO/img/plot_0019.png)<br>11:00 |
| [![LiveOcean surface currents](data/latest-LO/thumbs/plot_0020.png)](data/latest-LO/img/plot_0020.png)<br>12:00 | [![LiveOcean surface currents](data/latest-LO/thumbs/plot_0021.png)](data/latest-LO/img/plot_0021.png)<br>13:00 | [![LiveOcean surface currents](data/latest-LO/thumbs/plot_0022.png)](data/latest-LO/img/plot_0022.png)<br>14:00 |
| [![LiveOcean surface currents](data/latest-LO/thumbs/plot_0023.png)](data/latest-LO/img/plot_0023.png)<br>15:00 | [![LiveOcean surface currents](data/latest-LO/thumbs/plot_0024.png)](data/latest-LO/img/plot_0024.png)<br>16:00 | [![LiveOcean surface currents](data/latest-LO/thumbs/plot_0025.png)](data/latest-LO/img/plot_0025.png)<br>17:00 |
| [![LiveOcean surface currents](data/latest-LO/thumbs/plot_0026.png)](data/latest-LO/img/plot_0026.png)<br>15:00 | [![LiveOcean surface currents](data/latest-LO/thumbs/plot_0026.png)](data/latest-LO/img/plot_0026.png)<br>16:00 | [![LiveOcean surface currents](data/latest-LO/thumbs/plot_0027.png)](data/latest-LO/img/plot_0027.png)<br>17:00 |


The [University of Washington's LiveOcean model](https://faculty.washington.edu/pmacc/LO/LiveOcean.html) is the source for this free data product generated with open source code. Thanks to physical oceanography professor, Dr. Parker MacCready and his partners, for this resource.

### Motivation and methods

This site presents hourly estimates of the surface currents in Puget Sound for the most recent day and the next two days. During a training session for the [Race to Alaska](https://r2ak.com), we enjoyed using LiveOcean's daily movie of currents. When you don't have an engine on your boat and instead are relying on human power to move around the Salish Sea, the surface currents really matter!

The movie format, however, was difficult to use when trying to understand the "current currents" -- the conditions near your human-powered sailboat during a specific hour. Especially on mobile phones, it was difficult to stop the mp4 at the right frame, and we found no easy way to toggle between adjacent hours. Go ahead, try it with the [latest LiveOcean surface current movie](https://faculty.washington.edu/pmacc/LO/p5_PS_speed_top.html).

Our solution is to use the free, open source tool [ffmpeg](https://ffmpeg.org/) in a simple [Python](https://www.python.org/) script to break the mp4 into separate .png files, one for each hour of modeled currents. Then we present those images so that they are easy to view and/or download to your phone or whatever other system you use as a sailor or tactician. Along the way, we archive the images for folks who might want to easily go back in time and study past current conditions, or make a movie of currents during some historical period.

### Support or Contact

Have questions? Email veirs@uw.edu or open an issue in the main branch of the [ps-currents repository](https://github.com/salish-sea/ps-currents).
