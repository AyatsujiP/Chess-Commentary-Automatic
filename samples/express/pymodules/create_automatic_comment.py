# -*- encoding: utf-8 -*-

import sys
import json
from io import StringIO
import chess
import chess.pgn
import chess.uci

TYPE = "dev"

def read_in():
    line = sys.stdin.readline()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(line)


def read_pgn(pgn_string):
    pgn = StringIO(pgn_string)
    
    return chess.pgn.read_game(pgn)


def create_san_list(game):
    board = game.board()
    moves = game.main_line()
    
    ret = []
    for i,m in enumerate(moves):
        ret.append(board.san(m))
        board.push(m)


    return (ret)

def iterate_moves(game,game_san_list):
    pv_num = 3
    
    #Stockfish読み込み
    engine = chess.uci.popen_engine("./stockfish")
    engine.uci()
    
    engine.setoption({'MultiPV':pv_num})
    
    info_handler = chess.uci.InfoHandler()
    engine.info_handlers.append(info_handler)
    
    board = game.board()
    moves = game.main_line()
    #ret = game.board().variation_san(moves)
    
    #初手
    engine.position(board)
    ans = engine.go(movetime=2000)
    #最善手と実際の手を表示
    print ("Move Ply 1. Best move: %s. Actual Move: %s" % ( board.san(ans[0]), game_san_list[0]))
    
    for i,m in enumerate(moves):
        board.push(m)
        engine.position(board)
        ans = engine.go(movetime=2000)
        
        #最善手と実際の手を表示
        print ("End Move Ply %d. Best move: %s. Actual Move: %s" % (i+2,board.san(ans[0]), game_san_list[i+1]))
        score = info_handler.info["score"][1].cp * (0.01 if i % 2 else -0.01)
        pv = info_handler.info["pv"][1]
        
        print ("Stockfish Calculate Vatiation: %s" % board.variation_san(pv))
        print ("Score: %2.2f" % (score,))

if __name__ == "__main__":
    # PGNを読む
    if TYPE in ["dev",]:
        lines = { "PGNtoAnalyze": "[Event \"JO\"]\r\n[Date \"2017.11.05\"]\r\n[White \"a\"]\r\n[Black \"a\"]\r\n[Result \"*\"]\r\n[ECO \"B02\"]\r\n[Opening \"Alekhine\'s defence\"]\r\n\r\n\r\n1.e4 Nf6 2.e5 Nd5 3.c4 Nb6 4.a4 d6 5.a5 N6d7 6.e6 fxe6 7.d4 Nf6 8.Bd3 e5 9.dxe5\r\ndxe5 10.Nc3 Bg4 11.Qa4+ Nc6 12.Qc2 e6 13.f3 Nb4 14.Bg6+ hxg6 15.Qxg6+ Ke7\r\n16.fxg4 Nd3+ 17.Ke2 Nxc1+ 18.Rxc1 Qd4 19.Nf3 Qxc4+ 20.Ke1 Qf4 21.Ne2 Qb4+ 22.Kf1\r\nQxa5 23.Ng5 Re8 24.Qf7+ Kd8 25.Nxe6+ Rxe6 26.Qxe6 Bd6 27.Rd1 Ne4 28.Qd5 Rf8+\r\n29.Kg1 Qb6+ 30.Nd4 exd4 31.Qxd4 Qxd4+ 32.Rxd4 Kc8 33.Rxd6 cxd6", "__proto__": {} }
    else:
        lines = read_in()
    pgn_string = lines['PGNtoAnalyze']
    
    #PGNを読みGame型に変更
    game = read_pgn(pgn_string)
    
    #リスト作成
    game_san_list = create_san_list(game)
    
    #Moveを繰り返しエンジンで評価させる
    iterate_moves(game,game_san_list)
    
    

    