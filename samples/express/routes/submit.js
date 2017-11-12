/*
 * PGNを受け取り、Pythonモジュールを呼び出すためのルーティングを実施する。
 */

exports.receive = function(req,res){

	var body = req.body;
	
	console.log(body);
	var ret = spawnPython(body);
	
	res.send("Analysis is in work...<br><br>");
};

exports.redirect = function(req,res){
	res.redirect("307","/");
}

function spawnPython(bodyJson){
	
	var spawn = require('child_process').spawn,
	py    = spawn('python3', ['./pymodules/create_automatic_comment.py']);
	
	var data = "",
	ret = "";
	py.stdout.setEncoding('utf8');
	
	
	py.stdout.on('data', function(data){
	  console.log(data);
	  ret += data;
	});
	py.stdout.on('end', function(){
	});
	py.stdin.write(JSON.stringify(bodyJson));
	py.stdin.end();
	
	return ret;

};