# Collective Movement Exploration
> A web application to explore and analyze collective movement datasets.

<p align="center"><img width=100% src="https://raw.githubusercontent.com/dbvis-eren-ck/collective-movement-exploration/master/media/collective-movement-exploration-pipeline.png"></p>

<br>

## Visualize the Collective Movement

5 Stickelback fish             |  151 Goldenshiner fish
:-------------------------:|:-------------------------:
 <img src="https://raw.githubusercontent.com/dbvis-eren-ck/collective-movement-exploration/master/media/Fish5.gif" width=100%> |  <img src="https://raw.githubusercontent.com/dbvis-eren-ck/collective-movement-exploration/master/media/Fish151-dc.gif" width=100%>



## Main Features

* User and role management
* Upload datasets
* Feature extraction and visualization
    * Speed, acceleration, distance to centroid
    * Centroid, medoid, convex hull, delaunay triangulation, voronoi diagram
    * Convex hull area, swarm speed, swarm acceleration
* Network generation based on similarity
* Hierarchical clustering exploration
* Spatial view
* Line Chart, trend chart
* Zoom, pan & drag, brushing, tooltip
* REST API
* Streaming
* Export as CSV

## Demo

You can test a fully working live demo [here](https://animals.dbvis.de/)

## Documentation

* __[Installation](https://github.com/dbvis-eren-ck/collective-movement-exploration/blob/master/doc/installation.md)__
* __[Input Files](https://github.com/dbvis-eren-ck/collective-movement-exploration/blob/master/doc/input.md)__
* __[Rest API](https://github.com/dbvis-eren-ck/collective-movement-exploration/blob/master/doc/rest.md)__

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [D3](https://d3js.org/) - Visualizations
* [jQuery](http://jquery.com/)
* [jQuery UI](http://jqueryui.com/)
* [Bootstrap 4](http://getbootstrap.com/)
* [Papaparse](http://papaparse.com/)
* [Webpack](https://github.com/webpack/webpack)
* [Python libraries](https://github.com/dbvis-eren-ck/collective-movement-exploration/blob/master/src/requirements.txt)

## Authors

* **Eren Cakmak** - *Initial work*
* **Lukas Weixler**

See also the list of [contributors](https://github.com/dbvis-eren-ck/collective-movement-exploration/graphs/contributors)

## License

Released under a GNU General Public License. See the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Thanks to Juri Buchmüller, Prof. Daniel Keim, Jolle Jolles, Prof. Dr. Alex Jordan and Prof. Dr. Iain Couzin for their direct support of this project
