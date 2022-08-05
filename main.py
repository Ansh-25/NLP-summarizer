from summarizer import Summarizer

BaseDir = "Sample texts\\"

Fname = "9-11_attacks"
# Fname = "cryptocurrency"
# Fname = "AI"

file_name = BaseDir + Fname + ".txt"

obj = Summarizer(file_name,3)

summary = obj.generate_summary()

print("\tSummary \n" , summary)

fout = open(f"Summaries\\{Fname}_summary.txt","w")
fout.write(summary)
fout.close()