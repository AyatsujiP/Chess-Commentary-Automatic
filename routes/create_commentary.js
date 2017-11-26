var spawn = require('child_process').spawn;


exports.start = function(req,res){

	py = spawn('python3',['./models/create_commentary.py'])
		
	//line = '{"result":[{"fen_position":"rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq d3 0 1","best_move":"d5","calculated_line":"d5 Bf4 Nf6 e3 Nc6 Nf3 h6 Nc3 e6 Nb5 Bb4+ c3 Ba5 Bd3 O-O","total_evaluation_score":0.9,"material":{"white":null,"black":null,"total":{"MG":0.13,"EG":0}},"imbalance":{"white":null,"black":null,"total":{"MG":0,"EG":0}},"pawn":{"white":null,"black":null,"total":{"MG":-0.02,"EG":-0.01}},"knight":{"white":{"MG":0.13,"EG":0},"black":{"MG":0.13,"EG":0},"total":{"MG":0,"EG":0}},"bishop":{"white":{"MG":-0.13,"EG":-0.39},"black":{"MG":-0.13,"EG":-0.39},"total":{"MG":0,"EG":0}},"rook":{"white":{"MG":-0.28,"EG":0},"black":{"MG":-0.28,"EG":0},"total":{"MG":0,"EG":0}},"queen":{"white":{"MG":0,"EG":0},"black":{"MG":0,"EG":0},"total":{"MG":0,"EG":0}},"mobility":{"white":{"MG":-0.23,"EG":-0.29},"black":{"MG":-0.76,"EG":-0.87},"total":{"MG":0.53,"EG":0.58}},"king_safety":{"white":{"MG":0.93,"EG":-0.06},"black":{"MG":0.81,"EG":-0.06},"total":{"MG":0.11,"EG":0}},"threats":{"white":{"MG":0,"EG":0.1},"black":{"MG":0,"EG":0.1},"total":{"MG":0,"EG":0}},"passed_pawn":{"white":{"MG":0,"EG":0},"black":{"MG":0,"EG":0},"total":{"MG":0,"EG":0}},"space":{"white":{"MG":0.57,"EG":0},"black":{"MG":0.34,"EG":0},"total":{"MG":0.23,"EG":0}},"_id":"5a1a4b41fcb77e0bf5dae5b1"},{"fen_position":"rnbqkbnr/ppp1pppp/8/3p4/3P4/8/PPP1PPPP/RNBQKBNR w KQkq d6 0 2","best_move":"Bf4","calculated_line":"Bf4 Bf5 e3 e6 Bd3 Nf6 Bxf5 exf5 Nf3 Bb4+ c3 Bd6 O-O Bxf4 exf4 O-O","total_evaluation_score":0.08,"material":{"white":null,"black":null,"total":{"MG":0,"EG":0}},"imbalance":{"white":null,"black":null,"total":{"MG":0,"EG":0}},"pawn":{"white":null,"black":null,"total":{"MG":0,"EG":0}},"knight":{"white":{"MG":0.13,"EG":0},"black":{"MG":0.13,"EG":0},"total":{"MG":0,"EG":0}},"bishop":{"white":{"MG":-0.13,"EG":-0.39},"black":{"MG":-0.13,"EG":-0.39},"total":{"MG":0,"EG":0}},"rook":{"white":{"MG":-0.28,"EG":0},"black":{"MG":-0.28,"EG":0},"total":{"MG":0,"EG":0}},"queen":{"white":{"MG":0,"EG":0},"black":{"MG":0,"EG":0},"total":{"MG":0,"EG":0}},"mobility":{"white":{"MG":-0.27,"EG":-0.36},"black":{"MG":-0.27,"EG":-0.36},"total":{"MG":0,"EG":0}},"king_safety":{"white":{"MG":0.81,"EG":-0.06},"black":{"MG":0.81,"EG":-0.06},"total":{"MG":0,"EG":0}},"threats":{"white":{"MG":0,"EG":0.1},"black":{"MG":0,"EG":0.1},"total":{"MG":0,"EG":0}},"passed_pawn":{"white":{"MG":0,"EG":0},"black":{"MG":0,"EG":0},"total":{"MG":0,"EG":0}},"space":{"white":{"MG":0.46,"EG":0},"black":{"MG":0.46,"EG":0},"total":{"MG":0,"EG":0}},"_id":"5a1a4b46fcb77e0bf5dae5b2"},{"fen_position":"rnbqkbnr/ppp1pppp/8/3p4/2PP4/8/PP2PPPP/RNBQKBNR b KQkq c3 0 2","best_move":"e6","calculated_line":"e6 Nf3 c5 cxd5 exd5 Nc3 Nc6 Bf4 Nf6 e3 c4 Be2 Be7 O-O O-O Ne5 Bf5 Nxc6 bxc6","total_evaluation_score":0.15,"material":{"white":null,"black":null,"total":{"MG":0.05,"EG":-0.06}},"imbalance":{"white":null,"black":null,"total":{"MG":0,"EG":0}},"pawn":{"white":null,"black":null,"total":{"MG":0.15,"EG":0.09}},"knight":{"white":{"MG":0.13,"EG":0},"black":{"MG":0.13,"EG":0},"total":{"MG":0,"EG":0}},"bishop":{"white":{"MG":-0.19,"EG":-0.39},"black":{"MG":-0.13,"EG":-0.39},"total":{"MG":-0.06,"EG":0}},"rook":{"white":{"MG":-0.28,"EG":0},"black":{"MG":-0.28,"EG":0},"total":{"MG":0,"EG":0}},"queen":{"white":{"MG":0,"EG":0},"black":{"MG":0,"EG":0},"total":{"MG":0,"EG":0}},"mobility":{"white":{"MG":-0.19,"EG":-0.19},"black":{"MG":-0.27,"EG":-0.36},"total":{"MG":0.08,"EG":0.17}},"king_safety":{"white":{"MG":0.81,"EG":-0.06},"black":{"MG":0.79,"EG":-0.06},"total":{"MG":0.03,"EG":0}},"threats":{"white":{"MG":0,"EG":0.1},"black":{"MG":0.19,"EG":0.21},"total":{"MG":-0.19,"EG":-0.11}},"passed_pawn":{"white":{"MG":0,"EG":0},"black":{"MG":0,"EG":0},"total":{"MG":0,"EG":0}},"space":{"white":{"MG":0.63,"EG":0},"black":{"MG":0.46,"EG":0},"total":{"MG":0.17,"EG":0}}}]}'
	line = req.body.analyzeString;	
	fen = req.body.fen;
	ret = "";
		
	py.stdout.on('data',function(data){
		ret += data;
	})
	
	py.stdout.on('end',function(end){
		//res.render('create_commentary',{"comment":ret})
		res.render('create_commentary',{"fen": fen, "comment":ret.replace(/\s*$/, "")})
		console.log('Return',ret);
	})
	
	py.stdin.write(line);
	py.stdin.end();
}