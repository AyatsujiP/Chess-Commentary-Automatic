var spawn = require('child_process').spawn;


exports.start = function(req,res){

	py = spawn('python3',['./models/create_commentary.py'])
		
	line = req.body.analyzeString;
	fen = req.body.fen;
	ret = [];
		
	py.stdout.on('data',function(data){
		ret = (String(data).replace(/\s*$/g, "").split("\n"));
	})
	
	py.stdout.on('end',function(end){	
		addPGN(ret,res,render);

		console.log('Return',ret);
	})
	
	py.stdin.write(line);
	py.stdin.end();
}

var addPGN = function(ret, res,callback){
	for(var i = 0; i< ret.length;i++){
		ret[i] = "Ply " + String(i+1) + ": " +  ret[i];
	}
	callback(res);
}

var render = function(res){
	res.render('create_commentary',{"fen": fen, "comment":String(ret)})
}