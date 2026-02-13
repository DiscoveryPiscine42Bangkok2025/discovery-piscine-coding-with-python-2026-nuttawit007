#!/usr/bin/env python3
def find_king(board):
    king_position = None
    king_count = 0
    for index_r, val_r in enumerate(board):
        for index_c, val_c in enumerate(val_r):
            if val_c == 'K':
                king_position = (index_r, index_c)
                king_count += 1
    if king_count == 1:
        return king_position
    print("King not found or multiple kings present.")
    return None

def is_valid_board(board):
    """ตรวจสอบว่ากระดานเป็นสี่เหลี่ยมจัตุรัสมั้ย ด้วยการเช็คความยาวแต่ละแถว"""
    if not board:
        return False
    row_count = len(board) # จำนวนแถวในboard
    # print("row_count: " + str(row_count))
    if row_count > 8:
        print("Invalid board: exceeds maximum size of 8.")
        return False
    for row_line in board:
        # print("row str: " + row_line)
        if len(row_line) != row_count:
            print("Invalid board: not a square.")
            return False
    return True

def checkmate(board):
    """ ตรวจสอบความถูกต้องของกระดาน """
    if not is_valid_board(board):
        print("Fail")
        return

    """ หาตำแหน่งคิง """
    king_position = find_king(board) # (x, x) หรือ None
    if not king_position:
        print("Fail")
        return

    """ แยกตำแหน่งคิงเป็น row และ col """
    king_r, king_c = king_position

    """ วนลูปเพื่อหาตัวหมากศัตรูทั้งหมด """
    for row_enemy, val_r in enumerate(board):
        for col_enemy, enemy in enumerate(val_r):
            is_threat = False

            enemy_list = ["P", "R", "Q", "K", "B", "."]
            if enemy not in enemy_list:
                print("Invalid piece found on board.")
                return
            
            """ตรวจ Pawn"""
            if enemy == 'P':
                """Pawnจะรุกเมื่ออยู่แนวทแยงที่ติดกับคิง"""
                if row_enemy - king_r == 1 and abs(col_enemy - king_c) == 1: # P ต้องอยู่แถวล่างของ K และ อยู่แนวทแยง
                    print("Pawn attack detected.")
                    is_threat = True

            """ตรวจ Rook, Queen ในแนวตั้งและแนวนอน"""
            if enemy in 'RQ':
                """ตรวจแนวนอน"""
                if row_enemy == king_r:
                    print("Attack in the same row detected.")
                    is_threat = True
                
                """ตรวจแนวตั้ง"""
                if col_enemy == king_c and not is_threat:
                    print("Attack in the same column detected.")
                    is_threat = True

            """ตรวจ Bishop, Queen ในแนวทแยง"""
            if enemy in 'BQ': 
                """ตรวจแนวทแยง"""
                # ส่วนต่างระหว่าง row กับ col เท่ากันจะอยู่แนวทแยงกัน
                diff_row = abs(row_enemy - king_r)
                diff_col = abs(col_enemy - king_c)
                if diff_row == diff_col:
                    print("Attack in the same diagonal detected.")
                    is_threat = True

            """ถ้ารุกได้แสดง Success แล้วจบการทำงาน"""
            if is_threat:
                print("Success")
                return

    """วนลูปจนจบแล้วรุกไม่ได้"""
    print("Fail")