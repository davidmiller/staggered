// config/karma.config.js

module.exports = function(config){
  var opalPath = process.env.OPAL_LOCATION;

  var karmaDefaults = require(opalPath + '/opal/tests/js_config/karma_defaults.js');
  var baseDir = __dirname + '/..';

  var coverageFiles = [
    __dirname + '/../staggered/static/js/staggered/**/*.js',
    // Add code to include on test runs here ...
  ];

  var includedFiles = [
    'opal/app.js',

    // Add test cases here
    __dirname + '/../staggered/static/js/tests/**/*.js',
  ].concat(coverageFiles);

  var defaultConfig = karmaDefaults(includedFiles, baseDir, coverageFiles);
  config.set(defaultConfig);
};