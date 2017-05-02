/*eslint-disable no-unused-lets*/
/*global window, $, parameters, */

'use strict';

let JSONAPI_MIMETYPE = 'application/vnd.api+json';

var animalNameSpace = animalNameSpace || {};
animalNameSpace.dataset = [];
animalNameSpace.datasetMetadata = [];
animalNameSpace.swarmData = [];
animalNameSpace.dataSetPercentile = {};
animalNameSpace.indexTime = 0;
var source;

/**
 * Load the movement data with ajax queries
 * Afterwards if all ajax queries are finished
 * draw the group view
 */
$(document).ready(function() {
    // console.log(parameters);

    if (window.EventSource) {
        source = new EventSource('/api/movement_only/' + parameters['id']);
        source.onmessage = function(e) {
            if (e.data === 'close') {
                source.close();
                // console.log(dataset);
                // if all ajax queries are compelte initialize
                (function() {
                    function checkPendingRequest() {
                        if ($.active > 0) {
                            window.setTimeout(checkPendingRequest, 100);
                        } else {
                            animalNameSpace.spatialView();
                        }
                    }
                    window.setTimeout(checkPendingRequest, 100);
                })();


            } else {
                var data = JSON.parse(e.data);
                animalNameSpace.dataset = animalNameSpace.dataset.concat(data);
            }
        };

        source.addEventListener('error', function(e) {
            if (e.readyState == EventSource.CLOSED) {
                alert('Streaming error');
            }
        }, false);
    } else {
        alert('Webbrowser does not support streaming');
    }

    // ajax query to get the first page of the movement dataset
    $.ajax({
        url: '/api/percentile/' + parameters['id'],
        dataType: 'json',
        type: 'GET',
        contentType: 'application/json; charset=utf-8',
        headers: {
            'Accept': JSONAPI_MIMETYPE
        },
        success: function(data) {
            // convert the dataSetPercentile into an array
            // [min, percentile_1,...,percentile_9,max]
            for (let i = 0; i < data.length; i++) {
                animalNameSpace.dataSetPercentile[data[i]['feature']] = [data[i]['min'], data[i]['p1'], data[i]['p2'], data[i]['p3'], data[i]['p5'], data[i]['p7'], data[i]['p8'], data[i]['p9'], data[i]['max']];
            }
        }
    });
    // get the swarm features for the line chart

    $.ajax({
        url: '/api/dataset/' + parameters['id'] + '/swarm_speed',
        dataType: 'json',
        type: 'GET',
        contentType: 'application/json; charset=utf-8',
        headers: {
            'Accept': JSONAPI_MIMETYPE
        },
        success: function(data) {
            // add the speed feature to the dataset
            for (let i = 0; i < data.length; i++) {
                animalNameSpace.swarmData.push({
                    'time': i,
                    'speed': +data[i]
                });
            }

            $.ajax({
                url: '/api/dataset/' + parameters['id'] + '/swarm_acceleration',
                dataType: 'json',
                type: 'GET',
                contentType: 'application/json; charset=utf-8',
                headers: {
                    'Accept': JSONAPI_MIMETYPE
                },
                success: function(data) {
                    // add the speed feature to the dataset
                    for (let i = 0; i < animalNameSpace.swarmData.length; i++) {
                        animalNameSpace.swarmData[i]['acceleration'] = +data[i];
                    }
                }
            });

            $.ajax({
                url: '/api/dataset/' + parameters['id'] + '/swarm_convex_hull_area',
                dataType: 'json',
                type: 'GET',
                contentType: 'application/json; charset=utf-8',
                headers: {
                    'Accept': JSONAPI_MIMETYPE
                },
                success: function(data) {
                    // add the speed feature to the dataset
                    for (let i = 0; i < animalNameSpace.swarmData.length; i++) {
                        animalNameSpace.swarmData[i]['convex_hull_area'] = +data[i];
                    }
                }
            });

            //get metadata information
            $.ajax({
                url: '/api/metadata/' + parameters['id'],
                dataType: 'json',
                type: 'GET',
                contentType: 'application/json; charset=utf-8',
                headers: {
                    'Accept': JSONAPI_MIMETYPE
                },
                success: function(data) {
                    // add the speed feature to the dataset
                    for (let i = 0; i < data.length; i++) {
                        animalNameSpace.datasetMetadata.push(data[i]);
                    }
                }
            });
        }
    });


});