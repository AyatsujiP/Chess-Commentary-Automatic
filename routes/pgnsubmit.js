/*
 * Action PGN Submit
 */

var evaluateBoard = require("../models/evaluate_board");
var async = require('async');
const Chessjs = require("chess.js").Chess;
const chess = new Chessjs();
const chessCurrent = new Chessjs();
const startPos = chessCurrent.fen();

exports.start = function(req,res){
	var body = req.body;
	var analyzeResult = "";
	var analyzeResults = [];
	var ct = 0;
	var pgn = body.PGNtoAnalyze.replace('/\+/g',' ');


	chess.load_pgn(pgn);
	var fens = chess.history().map(move => {
		  chessCurrent.move(move);

		  return chessCurrent.fen();
	});
	console.log(fens);
				
	async.forEachSeries(fens,function(fen,callback){
		evaluator = new evaluateBoard.EvaluateBoard(fen,2);
		
		evaluator.executeCallbackfuncAfterEvaluationFinish( function(){
			ct += 1;
		    console.log(ct + " Res:");
		    console.log(evaluator.analysis_result);
		    analyzeResults.push(evaluator.analysis_result);
		    if (ct == fens.length){
		    	res.render("pgnsubmit",{"analyzeResult":JSON.stringify(analyzeResults),"PGNtoAnalyze": pgn});
		    	console.log(pgn);
		    }
		});
		setTimeout(callback, 7 * 1000);
	},
	console.log("Finish Eval!"));
}