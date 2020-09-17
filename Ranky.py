# Importing necessary modules
from re import findall
from requests import get
from flask import Flask, render_template

# Starting of Solve Count
def toph(link):
	if link == "":
		return "0"
	else:
		return findall(r'<div class=value>(.*?)</div>', get(link).text)[1]

def dimik(link):
	if link == "":
		return "0"
	else:
		return findall(r'<p class="h4">(.*?) <small>টি সঠিক সমাধান</small></p>', get(link).text)[0]

def uri(link):
	if link == "":
		return "0"
	else:
		return findall(r'<span>Solved:</span>\s*(.*?)\s*</li>', get(link).text)[0]

# Starting of main framework
app = Flask(__name__)
@app.route("/")
def ranky():
	''' Data list contains all users info. Each user's info must be a list.
	First Element: 0 (int)
	Second Element: name (str)
	Third Element: username (str)
	Fourth Element: toph link (str)
	Fifth Element: dimik link (str)
	Sixth Element: uri link (str)
Note: If any user does not have an account leave there an empty string. 	'''
	data = [
    [0, "Mahinul Islam", "mahin", "", "", "https://urionlinejudge.com.br/judge/en/profile/239509"],
    [0, "Majedul Islam", "majed", "", "", "https://urionlinejudge.com.br/judge/en/profile/229317"],
    [0, "Md. Mushfiqur Rahman", "mdvirus", "https://toph.co/u/mdvirus", "https://dimikoj.com/users/53/mdvirus", "https://urionlinejudge.com.br/judge/en/profile/223624"],
    [0, "Md. Shazzad Hossein Shakib", "HackersBoss", "https://toph.co/u/HackersBoss", "", ""],
    [0, "Abdullah Al Mukit", "newbie_mukit", "https://toph.co/u/newbie_mukit", "", "https://urionlinejudge.com.br/judge/en/profile/228785"],
    [0, "Md. Toukir Ahammed", "toukir48bit", "https://toph.co/u/toukir48bit", "", ""],
    [0, "Md. Sifat Al Imtiaz", "SifatTheCoder", "https://toph.co/u/SifatTheCoder", "", ""],
    [0, "Mojahidul Islam Rakib", "HelloRakib", "https://toph.co/u/HelloRakib", "", ""],
    [0, "Md. Forhad Islam", "fiveG_coder", "https://toph.co/u/fiveG_coder", "", ""],
    [0, "Most Rumana Akter Rupa", "programmer_upa", "https://toph.co/u/programmer_upa", "", ""],
    [0, "Most Keya Akter", "Uniqe_coder", "https://toph.co/u/Uniqe_coder", "", ""],
    [0, "Most Nargiz Akter", "Simple_coder", "https://toph.co/u/Simple_coder", "", ""],
    [0, "Most Masuda Akter Momota", "itsmomota", "https://toph.co/u/itsmomota", "", ""],
    [0, "Lutfor Rahman", "Scanfl", "https://toph.co/u/Scanfl", "", ""],
    [0, "Most Aysha Akter Borsha", "Smart_coder", "https://toph.co/u/Smart_coder", "", ""]
	]
	
	# Replacing the links with score
	for i in range(data.__len__()):
		data[i][3] = toph(data[i][3])
		data[i][4] = dimik(data[i][4])
		data[i][5] = uri(data[i][5])
		# Total score
		data[i][0]=int(data[i][3])+int(data[i][4])+int(data[i][5])
	
	# Sorting the data according to total score
	data = sorted(data, reverse=True)
	
	# Returning the data
	return render_template("ranky.html", data = data)

if __name__ == '__main__':
	app.run(debug = True)