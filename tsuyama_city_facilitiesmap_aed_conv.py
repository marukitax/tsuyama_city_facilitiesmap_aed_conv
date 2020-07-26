#
# 津山市オープンデータ（施設情報変換）
#
import sys
import argparse
import csv

print ('＊津山市オープンデータ変換：施設情報（ＡＥＤ）')

def get_args():

	parser = argparse.ArgumentParser()

	parser.add_argument("inputCSV",  help="入力ＣＳＶ（オープンデータＣＳＶ）", type=str)
	parser.add_argument("outputCSV", help="出力ＣＳＶ（アップロード用ＣＳＶ）", type=str)
	parser.add_argument("update",    help="更新日(YYYYMMDD)", type=str)

	args = parser.parse_args()

	return(args)

def main():
	args = get_args()

	print ("入力ＣＳＶ："+args.inputCSV)
	print ("出力ＣＳＶ："+args.outputCSV)
	print ("更　新　日："+args.update)

	with open(args.inputCSV, 'r') as f_in1:
		with open(args.outputCSV, 'w', encoding="utf_8_sig") as f_ot1:
			reader = csv.reader(f_in1)
			writer = csv.writer(f_ot1,lineterminator='\n')
			writer.writerow(['緯度', '経度', '更新日', 'コンテンツ'])
			header = next(reader)	# ヘッダー読み飛ばし
			for row in reader:
				data = [row[6],row[5]]																# 緯度、経度
				data.append('<strong>'+row[0]+'</strong><br>'+row[1]+'<br>'+row[2]+'<br>'+row[3])	#コンテンツ（施設情報）
				data.append(args.update)															# 更新日
				writer.writerow(data)

if __name__ == '__main__':
	main()

