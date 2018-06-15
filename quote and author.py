from requests import get
n=int(input("how many quotes do you want to fetch:\n"))
#f=open("author.txt","a")
for i in range(0,n):
    try:
        f=open("author.txt","a+")
        r=get("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json&json=?")
        d=r.json()
        for key in d.keys():
            a=str("author:"+d['quoteAuthor']+'\n')
            f.write(a)
            b=str("quote:"+d['quoteText']+'\n')
            f.write(b)
            c="-"*50
            f.write(c)
    except Exception as e:
        d['quoteText']=d['quoteText'].replace('//','/')
        h=str("author:"+d['quoteAuthor']+'\n')
        f.write(h)
        e=str("quote:"+d['quoteText']+'\n')
        f.write(e)
        ff="-"*50
        f.write(ff)
        f.close()
#f.close()
