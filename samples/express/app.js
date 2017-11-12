
/**
 * Module dependencies.
 */

var express = require('express')
  , routes = require('./routes')
  , user = require('./routes/user')
  , http = require('http')
  , path = require('path');

var app = express();

// additional install module
var analyze = require('./routes/analyze');
var submit = require('./routes/submit');
var bodyparser = require('body-parser');

// all environments
app.set('port', process.env.PORT || 8008);
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.use(express.favicon());
app.use(express.logger('dev'));
app.use(express.bodyParser());
app.use(express.methodOverride());
app.use(app.router);
app.use(express.static(path.join(__dirname, 'public')));

// to handle POST
app.use(bodyparser.urlencoded({extended: true}));

// development only
if ('development' == app.get('env')) {
  app.use(express.errorHandler());
}


//routing
app.get('/', routes.index);
app.get('/users', user.list);

app.get('/analyze', analyze.start);
app.get('/submit', submit.receive);
app.post('/submit', submit.receive);

http.createServer(app).listen(app.get('port'), function(){
  console.log('Express server listening on port ' + app.get('port'));
});
