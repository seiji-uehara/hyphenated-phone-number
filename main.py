import subfile_city  # 別ファイル読込(subfile_city.py)
import subfile_other # 別ファイル読込(subfile_other.py)
import re            # 正規表現
import unicodedata   # 全角→半角変換
import tkinter as tk
import tkinter.messagebox as messagebox


def run_button():
    # 初期化
    output_tel.configure(state = "normal")
    output_type.configure(state = "normal")
    output_pref.configure(state = "normal")
    output_area.configure(state = "normal")
    output_tel.delete(0, tk.END)
    output_type.delete(0, tk.END)
    output_pref.delete(0, tk.END)
    output_area.delete(0, tk.END)

    str = input_box.get()
    
    input_tel = re.sub(r"\D", "", unicodedata.normalize("NFKC", str))
    if len(input_tel) == 10 or len(input_tel) == 11:
        list_search = list(filter(lambda item : item["no"] == input_tel[:4], subfile_other.list_other1))
        if len(list_search) != 0: # リストが空ではない場合
            dict_search = list_search[0]
            if len(input_tel) == dict_search["digits_total"]:
                output_tel.insert(0, dict_search["no"] + "-" + input_tel[dict_search["digits_1st"]:dict_search["digits_1st"] + dict_search["digits_2nd"]] + "-" + input_tel[-1 * dict_search["digits_3rd"]:])
                output_type.insert(0, dict_search["type"])
                #input_box.delete(0, tk.END)
            else:
                errmsg("桁数不一致のためエラーが発生しました。")
        else:
            list_search = list(filter(lambda item : item["no"] == input_tel[:3], subfile_other.list_other2))
            if len(list_search) != 0: # リストが空ではない場合
                dict_search = list_search[0]
                if len(input_tel) == dict_search["digits_total"]:
                    output_tel.insert(0, dict_search["no"] + "-" + input_tel[dict_search["digits_1st"] :dict_search["digits_1st"] + dict_search["digits_2nd"]] + "-" + input_tel[-1 * dict_search["digits_3rd"]:])
                    output_type.insert(0, dict_search["type"])
                    #input_box.delete(0, tk.END)
                else:
                    errmsg("桁数不一致のためエラーが発生しました。")
            else:
                list_search = list(filter(lambda item : item["no"] == input_tel[:6], subfile_city.list_city))
                if len(list_search) != 0: # リストが空ではない場合
                    dict_search = list_search[0]
                    output_tel.insert(0, dict_search["area_code"] + "-" + dict_search["city_code"] + "-" + input_tel[-4:])
                    output_type.insert(0, "固定電話")
                    output_pref.insert(0, dict_search["pref"])
                    output_area.insert(0,  dict_search["ma"])
                    #input_box.delete(0, tk.END)
                else:
                    errmsg("無効な電話番号です。")
    elif len(str) == 0:
        errmsg("未入力です。")
    else:
        errmsg("桁数不一致のためエラーが発生しました。")
    
    output_tel.configure(state = "readonly")
    output_type.configure(state = "readonly")
    output_pref.configure(state = "readonly")
    output_area.configure(state = "readonly")


def errmsg(msg):
    output_tel.configure(state = "readonly")
    output_type.configure(state = "readonly")
    output_pref.configure(state = "readonly")
    output_area.configure(state = "readonly")
    messagebox.showwarning("エラー", msg)


# -------------------------------------------------------------------------------------------
# ウィンドウを作成
root = tk.Tk()
# タイトルを指定
root.title("ハイフン付き電話番号に変換")
# サイズを指定
root.geometry("400x270")
# ウィンドウサイズを固定
root.resizable(width=False, height=False)


# -------------------------------------------------------------------------------------------
# ラベルを設置
label_main = tk.Label(root, text = "電話番号を入力してください。", font = ("BIZ UDゴシック", "12"))
label_main.pack(pady = 10)

# テキストボックスを設置
input_box = tk.Entry(width = 40, font = ("BIZ UDゴシック", "12"))
input_box.pack(pady = 0)

# 実行ボタンを設置
button = tk.Button(root, text = "実行", font = ("BIZ UDゴシック", "12"))
button.pack(pady = 15)
button["command"] = run_button


# -------------------------------------------------------------------------------------------
# 1行目
frame_tel = tk.Frame(root)
frame_tel.pack(anchor = tk.W, pady = 5)

# ラベルを設置
label_tel = tk.Label(frame_tel, width = 10, text = "電話番号", font = ("BIZ UDゴシック", "12"))
label_tel.pack(side = tk.LEFT)

# 出力結果用テキストボックスを設置
output_tel = tk.Entry(frame_tel, width = 30, font = ("BIZ UDゴシック", "12"))
output_tel.pack(side = tk.LEFT)
output_tel.configure(state = "readonly")


# -------------------------------------------------------------------------------------------
# 2行目
frame_type = tk.Frame(root)
frame_type.pack(anchor = tk.W, pady = 5)

# ラベルを設置
label_type = tk.Label(frame_type, width = 10, text = "種別", font = ("BIZ UDゴシック", "12"))
label_type.pack(side = tk.LEFT)

# 出力結果用テキストボックスを設置
output_type = tk.Entry(frame_type, width = 30, font = ("BIZ UDゴシック", "12"))
output_type.pack(side = tk.LEFT)
output_type.configure(state = "readonly")


# -------------------------------------------------------------------------------------------
# 3行目
frame_pref = tk.Frame(root)
frame_pref.pack(anchor = tk.W, pady = 5)

# ラベルを設置
label_pref = tk.Label(frame_pref, width = 10, text = "都道府県", font = ("BIZ UDゴシック", "12"))
label_pref.pack(side = tk.LEFT)

# 出力結果用テキストボックスを設置
output_pref = tk.Entry(frame_pref, width = 30, font = ("BIZ UDゴシック", "12"))
output_pref.pack(side = tk.LEFT)
output_pref.configure(state = "readonly")


# -------------------------------------------------------------------------------------------
# 4行目
frame_area = tk.Frame(root)
frame_area.pack(anchor = tk.W, pady = 5)

# ラベルを設置
label_area = tk.Label(frame_area, width = 10, text = "エリア", font = ("BIZ UDゴシック", "12"))
label_area.pack(side = tk.LEFT)

# 出力結果用テキストボックスを設置
output_area = tk.Entry(frame_area, width = 30, font = ("BIZ UDゴシック", "12"))
output_area.pack(side = tk.LEFT)
output_area.configure(state = "readonly")


# -------------------------------------------------------------------------------------------
# ウィンドウ状態を維持
root.mainloop()