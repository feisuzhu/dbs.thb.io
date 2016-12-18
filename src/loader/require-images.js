var _ = require("lodash");

module.exports = function(content) {
  var l = [];
  var walk = function(o) {
    _.map(o, function(v) {
      if(_.isObject(v) || _.isArray(v)) {
        walk(v);
      }
      if(_.isString(v) && /\.(png|jpg|svg|gif)$/.test(v)) {
        l.push(v);
      }
    });
  }
  walk(JSON.parse(content));
  return _.join(_.map(l, function(v) { return 'require("' + v + '")'; }), ';');
}
