# -*- coding: utf-8 -*-
"""
解析結果を標準入力から受け取ってコメントを出力するモジュール。
Python(3.5)でモック作成、javascriptで書き直す可能性あり。
"""

import sys
import json

env = "node"

class CreateCommentary():
    
    def __init__(self):
        self.analyze_json = None
        self.comments = []
    
    def read_in(self):
        if env in ["dev",]:
            line = '{"result":[{"fen_position":"rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1","best_move":"e6","calculated_line":"e6 d4 d5 exd5 exd5 Qe2+ Qe7 Nc3 Nf6 Bf4 Nc6 O-O-O Qxe2 Ngxe2","total_evaluation_score":0.91,"material":{"white":null,"black":null,"total":{"MG":0.13,"EG":0}},"imbalance":{"white":null,"black":null,"total":{"MG":0,"EG":0}},"pawn":{"white":null,"black":null,"total":{"MG":-0.02,"EG":-0.01}},"knight":{"white":{"MG":0.13,"EG":0},"black":{"MG":0.13,"EG":0},"total":{"MG":0,"EG":0}},"bishop":{"white":{"MG":-0.13,"EG":-0.39},"black":{"MG":-0.13,"EG":-0.39},"total":{"MG":0,"EG":0}},"rook":{"white":{"MG":-0.28,"EG":0},"black":{"MG":-0.28,"EG":0},"total":{"MG":0,"EG":0}},"queen":{"white":{"MG":0,"EG":0},"black":{"MG":0,"EG":0},"total":{"MG":0,"EG":0}},"mobility":{"white":{"MG":-0.19,"EG":-0.21},"black":{"MG":-0.76,"EG":-0.87},"total":{"MG":0.57,"EG":0.66}},"king_safety":{"white":{"MG":0.97,"EG":-0.06},"black":{"MG":0.88,"EG":-0.06},"total":{"MG":0.08,"EG":0}},"threats":{"white":{"MG":0,"EG":0.1},"black":{"MG":0,"EG":0.1},"total":{"MG":0,"EG":0}},"passed_pawn":{"white":{"MG":0,"EG":0},"black":{"MG":0,"EG":0},"total":{"MG":0,"EG":0}},"space":{"white":{"MG":0.57,"EG":0},"black":{"MG":0.34,"EG":0},"total":{"MG":0.23,"EG":0}},"_id":"5a1a447529f4a70b5adaa2ed"},{"fen_position":"rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq e6 0 2","best_move":"Nf3","calculated_line":"Nf3 Nf6 Nc3 Nc6 Bc4 Bc5 O-O d6 a3 O-O d3 Bd7 Bd2","total_evaluation_score":0.08,"material":{"white":null,"black":null,"total":{"MG":0,"EG":0}},"imbalance":{"white":null,"black":null,"total":{"MG":0,"EG":0}},"pawn":{"white":null,"black":null,"total":{"MG":0,"EG":0}},"knight":{"white":{"MG":0.13,"EG":0},"black":{"MG":0.13,"EG":0},"total":{"MG":0,"EG":0}},"bishop":{"white":{"MG":-0.13,"EG":-0.39},"black":{"MG":-0.13,"EG":-0.39},"total":{"MG":0,"EG":0}},"rook":{"white":{"MG":-0.28,"EG":0},"black":{"MG":-0.28,"EG":0},"total":{"MG":0,"EG":0}},"queen":{"white":{"MG":0,"EG":0},"black":{"MG":0,"EG":0},"total":{"MG":0,"EG":0}},"mobility":{"white":{"MG":-0.19,"EG":-0.21},"black":{"MG":-0.19,"EG":-0.21},"total":{"MG":0,"EG":0}},"king_safety":{"white":{"MG":0.88,"EG":-0.06},"black":{"MG":0.88,"EG":-0.06},"total":{"MG":0,"EG":0}},"threats":{"white":{"MG":0,"EG":0.1},"black":{"MG":0,"EG":0.1},"total":{"MG":0,"EG":0}},"passed_pawn":{"white":{"MG":0,"EG":0},"black":{"MG":0,"EG":0},"total":{"MG":0,"EG":0}},"space":{"white":{"MG":0.46,"EG":0},"black":{"MG":0.46,"EG":0},"total":{"MG":0,"EG":0}},"_id":"5a1a447a29f4a70b5adaa2ee"},{"fen_position":"rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2","best_move":"Nc6","calculated_line":"Nc6 Bb5 Nf6 O-O Bd6 Re1 a6 Bxc6 dxc6 d4 Bg4 c3 Qe7 Qe2","total_evaluation_score":0.67,"material":{"white":null,"black":null,"total":{"MG":0.39,"EG":0.3}},"imbalance":{"white":null,"black":null,"total":{"MG":0,"EG":0}},"pawn":{"white":null,"black":null,"total":{"MG":0,"EG":0}},"knight":{"white":{"MG":0.06,"EG":0},"black":{"MG":0.13,"EG":0},"total":{"MG":-0.06,"EG":0}},"bishop":{"white":{"MG":-0.13,"EG":-0.39},"black":{"MG":-0.13,"EG":-0.39},"total":{"MG":0,"EG":0}},"rook":{"white":{"MG":-0.19,"EG":0},"black":{"MG":-0.28,"EG":0},"total":{"MG":0.09,"EG":0}},"queen":{"white":{"MG":0,"EG":0},"black":{"MG":0,"EG":0},"total":{"MG":0,"EG":0}},"mobility":{"white":{"MG":-0.19,"EG":-0.12},"black":{"MG":-0.27,"EG":-0.36},"total":{"MG":0.09,"EG":0.24}},"king_safety":{"white":{"MG":0.88,"EG":-0.06},"black":{"MG":0.83,"EG":-0.06},"total":{"MG":0.06,"EG":0}},"threats":{"white":{"MG":0.19,"EG":0.34},"black":{"MG":0,"EG":0.1},"total":{"MG":0.19,"EG":0.24}},"passed_pawn":{"white":{"MG":0,"EG":0},"black":{"MG":0,"EG":0},"total":{"MG":0,"EG":0}},"space":{"white":{"MG":0.46,"EG":0},"black":{"MG":0.46,"EG":0},"total":{"MG":0,"EG":0}},"_id":"5a1a448529f4a70b5adaa2ef"},{"fen_position":"r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3","best_move":"Bb5","calculated_line":"Bb5 Nd4 Nxd4 exd4 O-O c6 Bd3 d5 Re1 Be7 c3 Nf6 e5 Ng4 cxd4 O-O","total_evaluation_score":0.08,"material":{"white":null,"black":null,"total":{"MG":0,"EG":0}},"imbalance":{"white":null,"black":null,"total":{"MG":0,"EG":0}},"pawn":{"white":null,"black":null,"total":{"MG":0,"EG":0}},"knight":{"white":{"MG":0.06,"EG":0},"black":{"MG":0.06,"EG":0},"total":{"MG":0,"EG":0}},"bishop":{"white":{"MG":-0.13,"EG":-0.39},"black":{"MG":-0.13,"EG":-0.39},"total":{"MG":0,"EG":0}},"rook":{"white":{"MG":-0.19,"EG":0},"black":{"MG":-0.28,"EG":0},"total":{"MG":0.09,"EG":0}},"queen":{"white":{"MG":0,"EG":0},"black":{"MG":0,"EG":0},"total":{"MG":0,"EG":0}},"mobility":{"white":{"MG":-0.19,"EG":-0.12},"black":{"MG":-0.09,"EG":0.03},"total":{"MG":-0.09,"EG":-0.15}},"king_safety":{"white":{"MG":0.83,"EG":-0.06},"black":{"MG":0.83,"EG":-0.06},"total":{"MG":0,"EG":0}},"threats":{"white":{"MG":0,"EG":0.23},"black":{"MG":0,"EG":0.1},"total":{"MG":0,"EG":0.13}},"passed_pawn":{"white":{"MG":0,"EG":0},"black":{"MG":0,"EG":0},"total":{"MG":0,"EG":0}},"space":{"white":{"MG":0.46,"EG":0},"black":{"MG":0.46,"EG":0},"total":{"MG":0,"EG":0}},"_id":"5a1a448a29f4a70b5adaa2f0"},{"fen_position":"r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 3 3","best_move":"a6","calculated_line":"a6 Bxc6 dxc6 O-O Bg4 d3 Bd6 Nbd2 Ne7 h3 Be6 Ng5 Bd7 Nc4 O-O","total_evaluation_score":0.16,"material":{"white":null,"black":null,"total":{"MG":0.2,"EG":0.13}},"imbalance":{"white":null,"black":null,"total":{"MG":0,"EG":0}},"pawn":{"white":null,"black":null,"total":{"MG":0,"EG":0}},"knight":{"white":{"MG":0.06,"EG":0},"black":{"MG":0.06,"EG":0},"total":{"MG":0,"EG":0}},"bishop":{"white":{"MG":-0.19,"EG":-0.39},"black":{"MG":-0.13,"EG":-0.39},"total":{"MG":-0.06,"EG":0}},"rook":{"white":{"MG":-0.19,"EG":0},"black":{"MG":-0.28,"EG":0},"total":{"MG":0.09,"EG":0}},"queen":{"white":{"MG":0,"EG":0},"black":{"MG":0,"EG":0},"total":{"MG":0,"EG":0}},"mobility":{"white":{"MG":-0.13,"EG":-0.04},"black":{"MG":-0.09,"EG":0.03},"total":{"MG":-0.04,"EG":-0.07}},"king_safety":{"white":{"MG":0.83,"EG":-0.06},"black":{"MG":0.8,"EG":-0.06},"total":{"MG":0.03,"EG":0}},"threats":{"white":{"MG":0.18,"EG":0.41},"black":{"MG":0.15,"EG":0.19},"total":{"MG":0.03,"EG":0.22}},"passed_pawn":{"white":{"MG":0,"EG":0},"black":{"MG":0,"EG":0},"total":{"MG":0,"EG":0}},"space":{"white":{"MG":0.46,"EG":0},"black":{"MG":0.46,"EG":0},"total":{"MG":0,"EG":0}},"_id":"5a1a449029f4a70b5adaa2f1"},{"fen_position":"r1bqkbnr/1ppp1ppp/p1n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 0 4","best_move":"Bxc6","calculated_line":"Bxc6 dxc6 O-O Bg4 d3 Nf6 h3 Bxf3 Qxf3 Be7 Be3 O-O Nd2 Nd7 Qg4 Bf6 Nc4","total_evaluation_score":-0.35,"material":{"white":null,"black":null,"total":{"MG":0.23,"EG":0.17}},"imbalance":{"white":null,"black":null,"total":{"MG":0,"EG":0}},"pawn":{"white":null,"black":null,"total":{"MG":-0.08,"EG":-0.04}},"knight":{"white":{"MG":0.06,"EG":0},"black":{"MG":0.06,"EG":0},"total":{"MG":0,"EG":0}},"bishop":{"white":{"MG":-0.19,"EG":-0.39},"black":{"MG":-0.13,"EG":-0.39},"total":{"MG":-0.06,"EG":0}},"rook":{"white":{"MG":-0.19,"EG":0},"black":{"MG":-0.28,"EG":0},"total":{"MG":0.09,"EG":0}},"queen":{"white":{"MG":0,"EG":0},"black":{"MG":0,"EG":0},"total":{"MG":0,"EG":0}},"mobility":{"white":{"MG":-0.13,"EG":-0.04},"black":{"MG":-0.04,"EG":0.15},"total":{"MG":-0.09,"EG":-0.19}},"king_safety":{"white":{"MG":0.83,"EG":-0.06},"black":{"MG":0.8,"EG":-0.06},"total":{"MG":0.03,"EG":0}},"threats":{"white":{"MG":0.18,"EG":0.41},"black":{"MG":0.72,"EG":0.72},"total":{"MG":-0.54,"EG":-0.31}},"passed_pawn":{"white":{"MG":0,"EG":0},"black":{"MG":0,"EG":0},"total":{"MG":0,"EG":0}},"space":{"white":{"MG":0.46,"EG":0},"black":{"MG":0.46,"EG":0},"total":{"MG":0,"EG":0}},"_id":"5a1a449a29f4a70b5adaa2f2"},{"fen_position":"r1bqkbnr/1ppp1ppp/p1n5/4p3/B3P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 1 4","best_move":"Nf6","calculated_line":"Nf6 O-O d6 Bxc6+ bxc6 d4 Bg4 h3 Bxf3 Qxf3 exd4 Re1 c5 e5 dxe5 Rxe5+ Be7 Re2","total_evaluation_score":-0.41,"material":{"white":null,"black":null,"total":{"MG":0.08,"EG":0.08}},"imbalance":{"white":null,"black":null,"total":{"MG":0,"EG":0}},"pawn":{"white":null,"black":null,"total":{"MG":-0.08,"EG":-0.04}},"knight":{"white":{"MG":0.06,"EG":0},"black":{"MG":0.06,"EG":0},"total":{"MG":0,"EG":0}},"bishop":{"white":{"MG":-0.19,"EG":-0.39},"black":{"MG":-0.13,"EG":-0.39},"total":{"MG":-0.06,"EG":0}},"rook":{"white":{"MG":-0.19,"EG":0},"black":{"MG":-0.28,"EG":0},"total":{"MG":0.09,"EG":0}},"queen":{"white":{"MG":0,"EG":0},"black":{"MG":0,"EG":0},"total":{"MG":0,"EG":0}},"mobility":{"white":{"MG":-0.42,"EG":-0.29},"black":{"MG":-0.04,"EG":0.15},"total":{"MG":-0.38,"EG":-0.44}},"king_safety":{"white":{"MG":0.83,"EG":-0.06},"black":{"MG":0.83,"EG":-0.06},"total":{"MG":0,"EG":0}},"threats":{"white":{"MG":0.18,"EG":0.41},"black":{"MG":0.15,"EG":0.19},"total":{"MG":0.03,"EG":0.22}},"passed_pawn":{"white":{"MG":0,"EG":0},"black":{"MG":0,"EG":0},"total":{"MG":0,"EG":0}},"space":{"white":{"MG":0.46,"EG":0},"black":{"MG":0.46,"EG":0},"total":{"MG":0,"EG":0}}}]}'
        elif env in ["node",]:
            line = sys.stdin.readline()
        

        self.analyze_json = json.loads(line)["result"]
                       
        self.comments = ["" for i in range(0, len(self.analyze_json))]
        
        return 0
    
    def analyze(self):
        for i,tg in enumerate(self.analyze_json):
            analyze_string = ""
            if tg["best_move"] in ["(none)",]:
                analyze_string = "チェックメイト。"
            else:
                analyze_string += self.best_move(tg)
                analyze_string += self.best_line(tg)
                analyze_string += self.material_eval(tg)
                analyze_string += self.pieces_eval(tg)
                analyze_string += self.mobility_eval(tg)
                analyze_string += self.pawn_eval(tg)
                analyze_string += self.safety_eval(tg)
                analyze_string += self.passpawn_eval(tg)
                analyze_string += self.threat_eval(tg)
                analyze_string += self.space_eval(tg)
                
                
                analyze_string += self.evaluate(tg)
            
            self.comments[i] += analyze_string
        
        return 0
        
    def best_move(self,tg):
        return "この局面での最善手は" + tg["best_move"] + "。"
    
    def best_line(self,tg):
        line_length = 6
        line_moves = tg["calculated_line"].split(" ")[0:line_length]
        ret = "進行の一例は"
        to_move = tg["fen_position"].split(" ")[1]
        num = int(tg["fen_position"].split(" ")[5])
        
        #白の手番の場合
        if to_move in ["w",]:
            for i,m in enumerate(line_moves):
                if i%2 == 0:
                    ret += str(num) + "." + m
                else:
                    ret += " " + m + " "
                    num += 1
        else:
        #黒の手番の場合
            for i,m in enumerate(line_moves):
                if i==0:
                    ret += str(num) + "..." + m + " "
                    num += 1
                elif i%2 == 1:
                    ret += str(num) + "." + m
                else:
                    ret += " " + m + " "
                    num += 1
        
        return ret.rstrip(" ") + "。"
    
    
    def evaluate(self,tg):
        eval_score = float(tg["total_evaluation_score"])
        
        [w_win,w_better,w_good,w_slight, b_slight,b_good,b_better,b_win] = [5.00,2.50,1.00,0.50,-0.50,-1.00,-2.50,-5.00]

        ret = ["白勝勢", "白優勢","白有利", "白やや良し", "ほぼ互角", "黒やや良し", "黒有利", "黒優勢", "黒勝勢"]
        pointer = 4
        
        if eval_score > w_win:
            pointer = 0
        elif eval_score > w_better:
            pointer = 1
        elif eval_score > w_good:
            pointer = 2
        elif eval_score > w_slight:
            pointer = 3
        elif eval_score > b_slight:
            pointer = 4
        elif eval_score > b_good:
            pointer = 5
        elif eval_score > b_better:
            pointer = 6
        elif eval_score > b_win:
            pointer = 7
        else:
            pointer = 8
            
        return "この局面は" + ret[pointer] +"。"
    
    def material_eval(self,tg):
        material = float(tg["material"]["total"]["MG"]) + float(tg["material"]["total"]["EG"])
        
        if abs(material) < 1:
            return "大きな駒の損得はない。"
        elif material > 0 :
            return "白のほうが駒得、あるいは駒の効率が良い。"
        elif material < 0:
            return "黒のほうが駒得、あるいは駒の効率が良い。"
        
        
    
    def pieces_eval(self,tg):
        pieces = {"knight": float(tg["knight"]["total"]["MG"]) + float(tg["knight"]["total"]["EG"]),
                    "bishop": float(tg["bishop"]["total"]["MG"]) + float(tg["bishop"]["total"]["EG"]),
                    "rook": float(tg["rook"]["total"]["MG"]) + float(tg["rook"]["total"]["EG"]),
                    "queen": float(tg["queen"]["total"]["MG"]) + float(tg["queen"]["total"]["EG"])}

        #白駒得の場合
        if float(tg["material"]["total"]["MG"]) + float(tg["material"]["total"]["EG"]) > 0:
            sort = sorted(pieces.items(),key = lambda x: -x[1])
            
            return self.pieces_eval_return(sort, "白")
        
        #黒駒得の場合
        else:
            sort = sorted(pieces.items(),key = lambda x: x[1])
            return self.pieces_eval_return(sort, "黒")
            
    def pieces_eval_return(self,sort,col):
        if abs(sort[0][1]) > 0.3:
            if sort[0][0] in ["knight",]:
                return "ナイトの働きは"+col+"のほうが良い。"
            elif sort[0][0] in ["bishop",]:
                return "ビショップの働きは"+col+"のほうが良い。"
            elif sort[0][0] in ["rook",]:
                return "ルークの働きは"+col+"のほうが良い。"
            elif sort[0][0] in ["queen",]:
                return "クイーンの働きは"+col+"のほうが良い。"
        else:
            return ""        

    def mobility_eval(self,tg):
        mobility = float(tg["mobility"]["total"]["MG"]) + float(tg["mobility"]["total"]["EG"]);
        if mobility > 0.5:
            return "白のほうが駒が動かしやすい局面。"
        elif mobility < -0.5:
            return "黒のほうが駒が動かしやすい局面。"
        else:
            return ""

    def pawn_eval(self,tg):
        pawn = float(tg["pawn"]["total"]["MG"]) + float(tg["pawn"]["total"]["EG"]);
        if pawn > 0.5:
            return "白のほうがポーン形が良い。"
        elif pawn < -0.5:
            return "黒のほうがポーン形が良い。"
        else:
            return ""
    
    def threat_eval(self,tg):
        threat = float(tg["threats"]["total"]["MG"]) + float(tg["threats"]["total"]["EG"]);
        if threat > 0.5:
            return "白に狙いが多い局面。"
        elif threat < -0.5:
            return "黒に狙いが多い局面。"
        else:
            return ""
        
    def passpawn_eval(self,tg):
        passed_pawn = float(tg["passed_pawn"]["total"]["EG"]);
        if passed_pawn > 0.5:
            return "白のパスポーンが強い。"
        elif passed_pawn < -0.5:
            return "黒のパスポーンが強い。"
        else:
            return ""
                
    def safety_eval(self,tg):
        king_safety = float(tg["king_safety"]["total"]["MG"]) + float(tg["king_safety"]["total"]["EG"])
        if king_safety > 5.0:
            return "黒のキングは極めて危険な状態。"
        elif king_safety > 2.5:
            return "黒のキングは危険。"
        elif king_safety > 1.0:
            return "黒のキングはやや危険な状態。"
        elif king_safety < -5.0:
            return "白のキングは極めて危険な状態。"
        elif king_safety < -2.5:
            return "白のキングは危険。"
        elif king_safety < -1.0:
            return "白のキングはやや危険な状態。"
        else:
            return ""
    
    def space_eval(self,tg):
        space = float(tg["space"]["total"]["MG"]) + float(tg["space"]["total"]["EG"]);
        if space > 0.5:
            return "白のスペースが広い。"
        elif space < -0.5:
            return "黒のスペースが広い。"
        else:
            return ""
           
def main():
    cc = CreateCommentary()
    cc.read_in()
    cc.analyze()
    for comment in cc.comments:
        print (comment)

if __name__ == "__main__":
    main()
