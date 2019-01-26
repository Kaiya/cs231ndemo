import requests
import itertools
import time

import uncurl

# print(uncurl.parse("curl 'https://account.live.com/AddAssocId?ru=&cru=&fl=' -H 'Connection: keep-alive' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'Origin: https://account.live.com' -H 'Upgrade-Insecure-Requests: 1' -H 'Content-Type: application/x-www-form-urlencoded' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' -H 'Referer: https://account.live.com/AddAssocId?ru=&cru=&fl=' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7' -H 'Cookie: MUID=07462D7D021E6D2B18BF2144061E6E38; TOptOut=1; MSCC=1532961114; optimizelyEndUserId=oeu1532968527047r0.21518992146918103; wlidperf=FR=L&ST=1532969006027; PPLState=1; MH=MSFT; NAP=V=1.9&E=1526&C=tCEcI9CmuaGBF-DroSdDTRsWf7DdGq6_YzrvraSk5T_2AEmd_nvv6Q&W=1; ANON=A=B614183807FEB311A8EF27B8FFFFFFFF&E=1580&W=1; RPSAuth=FABmARQOIsqiBiVNmgLUgB%2B8kqQxgfQu%2BA5mAAAMgAAAEBYl1kYrJk8ju05L3v/pn6oQAenRrI6USrTwhkP9aZj48tqlh%2B2ogMmVP20TZdg9wJhjrGfs1mpnbQdGX93cbne3WG83hXt508Gb2dwg2vgdFMeSh34KA4mBTL30XUqsZ6DuAXyvhOuPrKKybozC4NMcsW6r1Gbk/GyuWfNEo0zrADarC5G6Ia6tY4URDOtolnq/y7Uht9kYPIzsiSB3NukiEtqSu6KEzUm%2BBvprfew01RESjZqc68VtxrZcCMj3DXKFVYDX0n2/Ykt%2BkHxty/xztQnHilqHFu0qiN/diH0jS78YXySJ5N9MNVJ7Grx3%2B1s1i9OYeL5WebI3QTm6/lX/hv21D9Gcwn1MmQEOm%2B%2B%2BbcbDypb/4xwNi5hfzrJkmtyNIABMnX5Z2CSnny2tWj/JY0OBWRSi6dhTIwTKpRd8FaNQrA%3D%3D; RPSSecAuth=FABmARQOIsqiBiVNmgLUgB%2B8kqQxgfQu%2BA5mAAAMgAAAENNb60Fru/TEuuSy1%2BDsYZ0QAUKcpsZQo8nlEzvw90N0IEE8wkaXhKrEiuGiiv60ZNa/1wwDMDOsDKno7gt5QZKfLhBOVTBFHOM7MlI3OCV92PxD387kjZZdWeOW2uD9ylCtRqT%2BpL9VKcWFi8IoRP5QARp%2BiTNBhqDiAKaptSq41A/vAPELkwj%2BV3NOVYMvkEDzIlbYZtf6/akU5SQ8Kbn3W3npTvZg0zZxpjY50j8SeFjki06qoHk79qfHeF4DcUMR7pGCYrbFveU8rzuL6Zxnzm%2BA0szY6sw0khaTtwtu2UpVIatju%2BqOPbrAyN3P%2B2FpChH8N8EoCnbpu1nZ2d/AFwt6oWiozq%2BKWxjDgdu3ebkV2JY1GFgK4B6wh2PgDWWUIACT2v3t6ArYCn6aFAMnEZ3P%2BAlkjHSw9uBj1cGq8sYHCQ%3D%3D; mkt=en-US; mkt1=en-US; amsc=QjGA1Ei40KuwQbfYCZEbVwQ5a/MozWNv7JlwUnnmwj2RWDw7QXz0d2VM1aahAdmGdQzZbiOopaalTavxRiyLBsC+WwnuxHBRTg2eG+VsLR5mkU8Y/S+YM5Zb7ngbRS5Na0J7k4wNe8h/Pvu5hF5JH5SJlWMNodGafIto69w1VG8NGj/Fyucpr7p0jM/PDDzqt2BraBAsQfdijujtTNAozbsW95k57nz1GrFqNFSFApS7nAjWuRIq5Cdr00vP8n/A:2:3c; MSPAuth=39APJ*dJhHlH3FptBs44I1EFdmRDxpV1Bzzyt1zZd!9awJDvCF5muxGIDxLfYCuDhoCakgYfgcqlKdL4yMW!H7z*nSATw*m8wWvo2Ity5PDliwVbuOlbH0!H7V!J!FDQ63yXN7m2X!11Y$; MSPProf=31D64fl!ZGXuYj8gKDPvvLgN*JEuU5btwFh*o60bqsSx2k7uAwuXRyRRFlEfFFyvnN40Gdd1wEb2U8Uvad0Qct*NDIbYNS49FcSwB20SL411wWE8ax5j1OTj44ZUyx*AHiPRTU4cu8q!*0Oz*7u2XxRA$$; WLSSC=EgAVAgMAAAAEgAAADAABYQC89HsKSg9kn8vTn/8KAPpMb4vPLuM213RNWFsn59gzlwK+ijELtk2rOvqISOMftgMvOAk53FsKlqRFxA8Koodx7nEdNJAR1/eTWyruFTdLbUCPhVFJ6yZ+PmshPMAxVKjkU908hNV9orLFCERZGufTAlFaab1HL0bmJzaeRWn5kwqI1GqO8oh/LLqdM4+PIdrFG3vBqutwiogJeobtIsHncZT0DcOl09RSqx169yE/rbECAhxZmIDNre3o/QW1QWheKocBJ4m8sAVjtPG9MHWnLypRf3qzlRX18qcBzVufKm0k2zLjwi9R+i1sD0q+hytMKJvyZuuN5erSQLnJDAQBeAAEAf2/AwDXowkVPUBfWy5AX1sQJwAAoBCgABAOAGt5QG91dGxvb2subHYAUgAAGmt5JW91dGxvb2subHZAcGFzc3BvcnQuY29tAAAAAUNOAAAAAAAABCYCAACG+FVAAAZDAAVrYWl5YQAFeGlvbmcAAAAAAAAAAAAAAAAAAAAAAACj4U1OgnKWUQAAPUBfWy7n1VsAAAAAAAAAAAAAAAAPADIxOC4xMDcuMTcuMjQ2AAIFAAAAAAAAAAAAAAAAEAQAAAAAAAAAAAAAAAAAAAAtn68H4FodhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM=; AMRPSAuth=FAAiARQq0UygULhJEGx7tOW5C1VUc59RuANmAAAEgAAACAM1LX2zqbHv4AA%2BLXJ7jPYSlf/3eNqLkdqWo0UCXsfMK4HQQB%2BdAriOqMy9OZ7EKR5L/kOrQ2jC3%2B2Ofd3n2D/eHBT/HrvPX2XvygHN2tSyJkIBVUk6UsKglyYZZJzqn7f5nSKjz1LmNo5HHzJVGBl4PL7mBqtPp2LT4S7rJxzBOrFhyWvSrh6bKk6chqULJ%2BH0fOEbyVtfmqpN7sSafjeSNr6f7GRYxwgBXcWpyCPAGc4a1lJHULk8o7xArL%2BXRrGhinkjao/oBNy8B2IK7iAzYgimU5mObBKv3dQvryrDKnTbx/OzuJSoaBQAUh7D89zNHfHNyzFAI8Ut6zYx6TI%3D; AMRPSSecAuth=FACaBhQq0UygULhJEGx7tOW5C1VUc59RuANmAAAEgAAACFBEy2tWaiISWAZHtfSw6dJpPwDSc5zjdUAQHZ3G2s4hErmKWkMCFBVyiDt6y3aKagJSftja6fczHoVVNjaLy8T1tDA8GxnZiC/YY3SZ6vQKQMPBKnDH%2BxiVVOd1hYPuhRM3vkT6kSus31YiWOmqAtcgtqKffJ073J/Zo%2Ba08IVOZxFPqPS%2ByMb%2BwypN46PBYRrPfe8tHjMUQvbffr0tQR2RabICW4JWChQqWzvAnGcksBOqZVw9wKFxirT9z5z0W4f7Yk0lA40Ng7QLFCjMHWisGSVchZgmMWKlY8fd7Qy9oFx9ZbCKv33mR3IjeTuJiQUfsIKlm80UiTZGTKiNNYOT7wRq7XaaFIQWU58RCn5KSpo/Z0LRk2LvvppDxjq9dKs6I/l7Ug90/H%2B8QJu82EMOB9ZK/uyapM9ufRa/16DOjAZNq%2BFIAeisxlsUvHaMOwTjrpcwu12Yrc%2BMBa87s3ujAx5t7u%2BPjw365zv1yBu%2B9M6tg1YDAv/6nkbEgKC8ji1ouOLtDTZZMQ2YEVncwY6C/Ibam%2BEfu2SPMU0HblFAk9EENSyDGfvGhpLAP%2BpGuV9FY7JBde44%2Bcv1nNLEqUWDQeRwambUr0jbvHbxwXJ90IMZxCL6f8mztCgJ%2ByItuyv7l5E10pqVgk1V07pER4ZXkwE1baw8b0aZLmKqmucRvDaknefeom1fWx/hWM5BWr3cN%2BUIKcJ7%2BX2%2BDT43ri5LtRZyblY7yijeAvKSU/qOBhI1rcvYkipGb%2BSDBdopStOXGAIkFEmyZxa5lEURZqS9h8efa5Ltx2mr9999ow9dH4NtQzLfUt/AEAAWNuomtW7Z4MvV7vk%2BOWLz9M2ascgwBPXNW/nh62LlHvxgnvUMspmUhveoYpVf%2BgbBDz%2Bm/1b98mItd2CM2fWoQXt/2UToR/GLwn4M/E%2BnNqwzuKjVHBQ1myjyDRnqPlUA9oud2jVNzF3idDcvdXyujHlLBlYdIjyDJZJR33Uksz1LWIN3tlOHAr7irkfIpWJgYhRJkPz7QXU/n2TMVYJ/Jd2ueTkmeSDR/LsSNRiml2ZmrsMDwDldzVTqKOxVVVfc8rRGAy5Pu7aXr6KOsc/VPFvFnB7TzQELxYuGJfc6EvG4KUzb4oBmMsWroLbqwvI8ZxfXRE8BhrhlqYCDvKMbgN5kHGZ0v94CcLaQKOknIYTGZ%2B01ecpRM0vGYySvGM4O9gLVwxU3nGUc8sNcAzKe45P6uhVacYP7pSOn3jdIrXwKias%2BOACEJ82k2sOKXBLQSXnafKygES6HloOSEkZg3HWj%2BtpxqFRIEHRUoeIRFE/D4uoWrXfg8B854m1ad9Wd6m/USGjHO47rZ7GciM9hB1VETyIZgiCC7xo9sOEkM07N5%2BR1J%2BdfpKqTFXiw4/kBBj5b1C6XG18/4zjAOz2187gOmZm3HPYJHaYl/AOqqWVMHorBj3%2BTS0dW%2Bcr%2BZSb9gs0jPioVtWkAnUh7MUY5jcfeKzQlrV827/PN/edLWO3Kk/6953syblCy2UOYDuaCsUPFmf9XMwzbwZ8Tru3BOnIyafsekGj2HVDn2tQLEAaspGFWGebkys1kb4YVXTqLASSjRELp%2BnAxAEtbhDj7XYENObx1yNc3kcek4l%2Bhc0ikvZlSXxgBHt6HXM9dkGIgwHTxWEsqH62oOxMYr6w0cat0IB/h/bKNv7VCXQzUVI/o26np8DFYz6ENJ4FwdPHpHCfz0vHLL005Lqm9cb7sjya7og/jXF15JhfZJ2iyt5TGN6OBE0Tt9AjlGrg4FRV5grHAsCcSuMOIG55JpNXRJwRBK4RWUO6VXn%2B8luWMoZ4LagUice2n7ZK/j%2Bwr3mRRGq4B7xUbEmunnOqBszPFvgRVDsXeZSEisXZsWV/sXfQyzx3C8GEEHy5VhxjlZYf7jcN8C0kT8eq5kH8QyxtgtMD3FgDXYPWqfZU/UQZ4MRcOz33/yhmD38g7q0xeISM16KoUa2uoUOkzOaow%2BS82Zv2ijIMHFb9%2Bm7Nbf%2BvgYEPCRQx7/H6rXJ10AVnh5MNZhryAJQo2XDY1LNkZR/yND/QamdV/9j5ZVx8vCFIEsJE8UUN4u5nb0YxC0iqq4Gg/6p4HmYexZ8rie7bTrVqiRazk4mVIw9PDrTWfC0ylSlA%2BNisZF56gPtDbczicTilOt1ic8ysPFACVQehu7JWu1A1jWQuDy8alt5/rQQ%3D%3D; ANON=; NAP=; AMSTATE=BBAG=256&CID=82729651a3e14d4e&RENAMERULENS=EASI-True--HOTMAIL-True--LIVE-True&NewMN=&UserNameQs=&SESSIONID=cda30494-4c84-440b-b3f0-c17d05ae84d6; CkTst=MX1532969130305' --data 'canary=cf%2BAkgobvya7NX8lcXkW%2BIWAmlX%2Bk5T6zejqvDQsd%2BU%3D2&PostOption=LIVE&SingleDomain=cqB7DKAaLt%2FHHzO0wcaJRQCJ%2BqUCDKJjKEMJGCVPCYGQlKxHL%2B2aG%2FkVsrF5zuEaHmDPDHMZiVFkZBPXI%2BTDAcIjDjz04e8qVr2Ix38DoiM%3D%3A2%3A3&UpSell=&AddAssocIdOptions=LIVE&AssociatedIdLive=l.l' --compressed"))

# print(uncurl.parse("curl 'https://account.live.com/AddAssocId?ru=&cru=&fl=' -H 'Connection: keep-alive' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'Origin: https://account.live.com' -H 'Upgrade-Insecure-Requests: 1' -H 'Content-Type: application/x-www-form-urlencoded' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' -H 'Referer: https://account.live.com/AddAssocId?ru=&cru=&fl=' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7' -H 'Cookie: MUID=07462D7D021E6D2B18BF2144061E6E38; TOptOut=1; MSCC=1532961114; optimizelyEndUserId=oeu1532997911461r0.6460919936895175; wlidperf=FR=L&ST=1532997987258; MH=MSFT; mkt=en-US; ANON=; NAP=; amsc=UcN/D3VTIlhYfkUiWp1N4EXZoF+qNaRqD40wEEs1LQ6ycjHd1m//dDTnMd2rtNme87P9SXc+8FhxgX4H7g7WUfcrdQ4lNpzplNcm4f1Ft9aAD9AO/IYj4zOMLJZEIbPhoC0x9dC+pKf5bbzNtS5yOCKcE014zYU3RaUsjxp2iSWN2heFnIfu9DJcx4eEQ732sLrvhSuYd9qWHroOGZsfst0WJJyqHMKRtWqv2ZrB+mMnWLiBmqsQQqi5hEweE7GN:2:3c; PPLState=1; NAP=V=1.9&E=1527&C=UhMIHp-9yDGKE9saUeODr_M-INN7-Vysikfz9vBiTrQL5XaBfRrXzg&W=2; ANON=A=1AAD4B1E611E32F23AB38286FFFFFFFF&E=1581&W=2; mkt1=en-US; MSPAuth=3RBCa263TG!Q4SPHaHEpESCK2MddKdsHNeoJaZNE0UUXuLKuk**ig5aQWxKB4W4BUeSeoKlnVVnqm61oGgH96wojzROBdOAhaUOKvjBpBzcTRTTEbiLiMx0djU*pNHJgLcP41xs*gdmhw$; MSPProf=3DIIkMudFFREn66VH0NySvqERzICdZzIH52p1BYB4kukC2awOUcNiasPm3u8iUJYf8fZBUI4ZIKmpPzlVf*A0uqe3GNV6X*eecQLDPWLgloVyaU2IKdq9jT5NPx6x9jUIS943CtGXrd1P6D04xPbQ2Dw$$; WLSSC=EgAXAgMAAAAEgAAADAABo2cs4ZiBIfGtz7em/irc/M+lW3ngeTMmwL9YsueElkk6uomD+4AfzoT+PXlkYmi+vaYX9sP/6s/Ru8IhHBUGCD3zQhqhNylbJEyWw/bE63abGRR4CaQcc4AYTWsPXZeF32qGFbcsERuztOFZWSKNIg8L03A6syeMJBH+zHJMYa/gAOZyzQvXhIhYZGYJQjtuPlzBJf8risMy+Xw2MLkGZ2TnsyQPd3u2REKPXA550EApzFwNDegBSQdsQqNxfL07Uw1YbN7IEIaCSeCERrRPWZxpgk/BDxAfZLRRVMCfEUGldViknno2h8///Hm+1z4LLf8/qfPwVovH+Qwx32jJyQYBeAAGAf5/AwAVOCYY9rRfW++0X1sQJwAAoBCgABgPAHhreUBvdXRsb29rLmF0AFMAABt4a3klb3V0bG9vay5hdEBwYXNzcG9ydC5jb20AAAABVVMAAAAAAAAMBwIAAIb4VUAABkMABUthaXlhAAVYaW9uZwAAAAAAAAAAAAAAAAAAAAAAANK26+lu7xcpAAD2tF9b71vWWwAAAAAAAAAAAAAAAA8AMzUuMjI5LjIyMS4xMDIABAEAAAAAAAAAAAAAAAAQBAAAAAAAAAAAAAAAAAAAAGIxl1q30EaWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAw==; AMRPSAuth=FAAiARQq0UygULhJEGx7tOW5C1VUc59RuANmAAAEgAAACIUVMrg%2BGEHL4AALk3fQI1BAJWSkIZVjRyxvTf0AO6mx9I8jh9gF9cdtoAyZ0SpVtYLv4Fk4EFw5ys9OW0AASHCMxg/7hBBoRzoTDKO/2Rz6Dvx3zmbHBytLzXbZk7cT96/TSfrbiqp8Mw%2BPH33njh2wUuhSc4v/PzPg5jtsKysTxC6DHzUSzX0O2jgVDdple8ArtMV1QZ13fIA0HOXjINZXGharBL2tJgadI0JSO2FPD7jwS1un0kz//3qgHo4h7xpLZAD3YFUKg%2Bjry8dwCho%2BS53uik8XJmESqfZjIEa5ksdgKtzAAgSebhQAMX9Q1TLg/GJofUSiG8bK%2BY//jh8%3D; AMRPSSecAuth=FACaBhQq0UygULhJEGx7tOW5C1VUc59RuANmAAAEgAAACPq44CC97eA1WAbdWBsBM9tKuplp/u7O25HW9g3gFNi2vaDK34fmVxjvzTfThCxHsDmsTdYkYqgh%2BvzL16MtTPLluMbel6/G8OrZ1YEzgl/it2coaPXJmFVqZQPBCbhMtby/eNv0P56olwAciKx4FeIMs96m3oxlCwzAsbKYKslFH4OsoPFxEoUoCpdje0w6htTzH7x6LegBfHVV30xH7mVnVrm7WdTRJpnPmrWKxZGV28pTY8Cox/JbGhmVu/EuaiMgKRu8do0lKadjnkOBQ0WWpiwxFQWmucJghAvDDMVzJM5AEJB3AGK6wautQB9JP9MsYPYyXaGcLD/iXGUSfbdmQSrb8qaAxaCPAkfhJl2fzjULoebLWZaV%2BEsyjB1D/Uq%2BeYKGTOHU0FR8Ef1A6RDd1RIZAes7gB4IYIG8XTjYnyekdqw85Z8TYowgkGhwahICpAkt3yc4FxegvEcIbOnjMHJP/P1vhyybUlFp74OeAKcsxNQM6EVrVbZOh3l3MtuZ1yYcTLWO3er7HiqNrVKYBU9hzaWvj1L%2BZuKvoYl6YePCBiOhXC5DfSN7tpaiSt80etdaAkKc0F20m8R8hq2T7/BWCxSobANpE15W6Sqt37Bii53RzYPKdxbEawYdLSnSojRN1uL%2BmArUsTs5L%2Bhnf14FJeFTMfJp7vmOwOrTV4CbQPsIJbLChrZk/z1fU%2BP0bzzvFJcZIHTcAq05wE3NnqBsfWynMqaAQ4hNgeM/%2BXlKQYPOhe7ST0UfSbLDqgPw3LVhNqQdjMdXeFQIQVF%2B/gENGdHExIf3u4IBoEwfy92VrmnJK6unKgyXQno3k1zkHtMUFqm7566mBjay0Tk3PpLVxw4MFJeeDbqwnNXy/XBd8HAiKkxNc/nhGhgtBc2hpFrx8wu3aRQvVlkB4y29ufjq96t22cMPgt2LdXtqsHPeYgQ1sJgp%2B1pNhQwijOU0UlNK8vLChjXmUmjLmhP3YSRL5u3ACMw9bFrIX1YpTMnz%2BQpqSZN2ue63Zey8S1Q7DhyO1jAtuQmh/pXXkIBCZtian5Llvo87%2BKiyQReyZheC96KzjIVHIzaw%2BT/X0lNmQt4n3ZuDpS5IUTvVHwsKXNsihnswaUUP3gk6KwWxg9fYGXDembE8e39Vq%2BS8VL8d/YO%2BRc8Qg41duOaqTomULuBM%2BJWNL22Z77fkSd5hq5dEprtnkQ8R3yH6Sj1iS9Z2Pu8F7odrPp719MfndRkmqCnEvEVAz17FCNCHEvY6M2q1Ve5GfWiu32otMiXwY7Ou36xY93Ya8DjTdfckUwSWGT8hrHVrXCeUR37p0hCYzaZKt2O43cIoLARTkdZhNo1CNSK%2B2IS2PMhqaYa7Q59b1d2i3ujirFM6eWvdlTAahJZ2qFjs9r4L051fXxOimEOpBv2Vm1a0AQco92TEYvHyLQotZoMo9jBrRFXLTLdmk8qOU/m3U7vGKFUz8myPd6q/jNwHg3bERxY7bAsPnUIoexDf96s2SllndamTZSb71sPZf/LflpJaLlZua2/8XEF%2BcgIMAXfwMMPNUmHjoFv2IDcgGVz9RtMXwusyUjeKq6OflccuLjiFOK5ovBFAgzp34nUxcXZL6sd88SZuLorLIp8mqIFB7khEKwS5D0D4sSCmrjCIF1ildpu7hmjhLOnJfE1/j5tQF2uLdGbdXJ/hB4AEdUywNxMx3Lp3%2BPP2j9i8JxbxwlcGbzE1wTgTgtCqHBaW4wcAmLel0Cvk8C8WwWM4UT15YGVeKHcQiGXCJBy9YKma2drEpef9TDa50cHLXTNqTqexRu%2BzxMmDfrHg/FsX6TMOxlLR%2BwzxVoaUzYNY%2BKeYBB9VIQfdTFrqWC2cyhnYPiDRkNtigmEqeiZX5VjHRkDTATpB/dizY00MvoMw9LpYfgIyizc%2Bm%2BpXrab4Ygd9QR8IRdgtRpSuf1g7NSQlkbwxpd4yFtXTVZYfFF54N6LTf3SQZLRAWwJSJYexZyTE9IAN6b2YEtozVBKPHkoQUSjZRhYGk42yXAxCfgRT8dN2OIHPxKV3TqZSigvC0I1aRABJMNerbAJEnD7poranJv7%2BS3o874aYT5wXqQu0X57%2B2MiG3OKbj4k3Vo5cDruR3NmSr3ds233rWNHg5nvVNbXsBeQRN57GdOQ3Lnyq357NXi6P4K9m7ZmaK%2B54FACKLTLdeQg6yWLlyduaQ8BkQ0bywA%3D%3D; rewardsinfo=en-us%3Ben-us%3Brewards; AMSTATE=BBAG=256&CID=6eef1729d2b6ebe9&RENAMERULENS=EASI-True--HOTMAIL-True--LIVE-True&NewMN=&UserNameQs=&SESSIONID=5efc8eee-acea-43f3-9543-6f1f19150aea; CkTst=MX1532998932538' --data 'canary=wxtKLi4cbheZFYL8i4G3eVa7oDAijC27ImnPGWFaVjA%3D8&PostOption=LIVE&SingleDomain=MTRwdz5HZoJEJtx6zI65UmQOGhraM%2FWxMepDYRCb0i27xuGa%2F8Gry6dkqRvjO8%2FIcw7pqalltXCDhXwjHXGpiOYNiL9QYu%2F5q8LMyetGfL0%3D%3A2%3A3&UpSell=&AddAssocIdOptions=LIVE&AssociatedIdLive=xky' --compressed"))




for i in itertools.permutations('abcdefghijklmnopqrstuvwxyz.', 2):
    # addressName = '.'.join(i)
    addressName = ''.join(i)
    print("trying: "+addressName)
    data = 'canary=wxtKLi4cbheZFYL8i4G3eVa7oDAijC27ImnPGWFaVjA%3D8&PostOption=LIVE&SingleDomain=MTRwdz5HZoJEJtx6zI65UmQOGhraM%2FWxMepDYRCb0i27xuGa%2F8Gry6dkqRvjO8%2FIcw7pqalltXCDhXwjHXGpiOYNiL9QYu%2F5q8LMyetGfL0%3D%3A2%3A3&UpSell=&AddAssocIdOptions=LIVE&AssociatedIdLive=' + addressName

    req = requests.post("https://account.live.com/AddAssocId?ru=&cru=&fl=",
    data=data,
    headers={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://account.live.com",
        "Pragma": "no-cache",
        "Referer": "https://account.live.com/AddAssocId?ru=&cru=&fl=",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    },
    cookies={
        "AMRPSAuth": "FAAiARQq0UygULhJEGx7tOW5C1VUc59RuANmAAAEgAAACIUVMrg%2BGEHL4AALk3fQI1BAJWSkIZVjRyxvTf0AO6mx9I8jh9gF9cdtoAyZ0SpVtYLv4Fk4EFw5ys9OW0AASHCMxg/7hBBoRzoTDKO/2Rz6Dvx3zmbHBytLzXbZk7cT96/TSfrbiqp8Mw%2BPH33njh2wUuhSc4v/PzPg5jtsKysTxC6DHzUSzX0O2jgVDdple8ArtMV1QZ13fIA0HOXjINZXGharBL2tJgadI0JSO2FPD7jwS1un0kz//3qgHo4h7xpLZAD3YFUKg%2Bjry8dwCho%2BS53uik8XJmESqfZjIEa5ksdgKtzAAgSebhQAMX9Q1TLg/GJofUSiG8bK%2BY//jh8%3D",
        "AMRPSSecAuth": "FACaBhQq0UygULhJEGx7tOW5C1VUc59RuANmAAAEgAAACPq44CC97eA1WAbdWBsBM9tKuplp/u7O25HW9g3gFNi2vaDK34fmVxjvzTfThCxHsDmsTdYkYqgh%2BvzL16MtTPLluMbel6/G8OrZ1YEzgl/it2coaPXJmFVqZQPBCbhMtby/eNv0P56olwAciKx4FeIMs96m3oxlCwzAsbKYKslFH4OsoPFxEoUoCpdje0w6htTzH7x6LegBfHVV30xH7mVnVrm7WdTRJpnPmrWKxZGV28pTY8Cox/JbGhmVu/EuaiMgKRu8do0lKadjnkOBQ0WWpiwxFQWmucJghAvDDMVzJM5AEJB3AGK6wautQB9JP9MsYPYyXaGcLD/iXGUSfbdmQSrb8qaAxaCPAkfhJl2fzjULoebLWZaV%2BEsyjB1D/Uq%2BeYKGTOHU0FR8Ef1A6RDd1RIZAes7gB4IYIG8XTjYnyekdqw85Z8TYowgkGhwahICpAkt3yc4FxegvEcIbOnjMHJP/P1vhyybUlFp74OeAKcsxNQM6EVrVbZOh3l3MtuZ1yYcTLWO3er7HiqNrVKYBU9hzaWvj1L%2BZuKvoYl6YePCBiOhXC5DfSN7tpaiSt80etdaAkKc0F20m8R8hq2T7/BWCxSobANpE15W6Sqt37Bii53RzYPKdxbEawYdLSnSojRN1uL%2BmArUsTs5L%2Bhnf14FJeFTMfJp7vmOwOrTV4CbQPsIJbLChrZk/z1fU%2BP0bzzvFJcZIHTcAq05wE3NnqBsfWynMqaAQ4hNgeM/%2BXlKQYPOhe7ST0UfSbLDqgPw3LVhNqQdjMdXeFQIQVF%2B/gENGdHExIf3u4IBoEwfy92VrmnJK6unKgyXQno3k1zkHtMUFqm7566mBjay0Tk3PpLVxw4MFJeeDbqwnNXy/XBd8HAiKkxNc/nhGhgtBc2hpFrx8wu3aRQvVlkB4y29ufjq96t22cMPgt2LdXtqsHPeYgQ1sJgp%2B1pNhQwijOU0UlNK8vLChjXmUmjLmhP3YSRL5u3ACMw9bFrIX1YpTMnz%2BQpqSZN2ue63Zey8S1Q7DhyO1jAtuQmh/pXXkIBCZtian5Llvo87%2BKiyQReyZheC96KzjIVHIzaw%2BT/X0lNmQt4n3ZuDpS5IUTvVHwsKXNsihnswaUUP3gk6KwWxg9fYGXDembE8e39Vq%2BS8VL8d/YO%2BRc8Qg41duOaqTomULuBM%2BJWNL22Z77fkSd5hq5dEprtnkQ8R3yH6Sj1iS9Z2Pu8F7odrPp719MfndRkmqCnEvEVAz17FCNCHEvY6M2q1Ve5GfWiu32otMiXwY7Ou36xY93Ya8DjTdfckUwSWGT8hrHVrXCeUR37p0hCYzaZKt2O43cIoLARTkdZhNo1CNSK%2B2IS2PMhqaYa7Q59b1d2i3ujirFM6eWvdlTAahJZ2qFjs9r4L051fXxOimEOpBv2Vm1a0AQco92TEYvHyLQotZoMo9jBrRFXLTLdmk8qOU/m3U7vGKFUz8myPd6q/jNwHg3bERxY7bAsPnUIoexDf96s2SllndamTZSb71sPZf/LflpJaLlZua2/8XEF%2BcgIMAXfwMMPNUmHjoFv2IDcgGVz9RtMXwusyUjeKq6OflccuLjiFOK5ovBFAgzp34nUxcXZL6sd88SZuLorLIp8mqIFB7khEKwS5D0D4sSCmrjCIF1ildpu7hmjhLOnJfE1/j5tQF2uLdGbdXJ/hB4AEdUywNxMx3Lp3%2BPP2j9i8JxbxwlcGbzE1wTgTgtCqHBaW4wcAmLel0Cvk8C8WwWM4UT15YGVeKHcQiGXCJBy9YKma2drEpef9TDa50cHLXTNqTqexRu%2BzxMmDfrHg/FsX6TMOxlLR%2BwzxVoaUzYNY%2BKeYBB9VIQfdTFrqWC2cyhnYPiDRkNtigmEqeiZX5VjHRkDTATpB/dizY00MvoMw9LpYfgIyizc%2Bm%2BpXrab4Ygd9QR8IRdgtRpSuf1g7NSQlkbwxpd4yFtXTVZYfFF54N6LTf3SQZLRAWwJSJYexZyTE9IAN6b2YEtozVBKPHkoQUSjZRhYGk42yXAxCfgRT8dN2OIHPxKV3TqZSigvC0I1aRABJMNerbAJEnD7poranJv7%2BS3o874aYT5wXqQu0X57%2B2MiG3OKbj4k3Vo5cDruR3NmSr3ds233rWNHg5nvVNbXsBeQRN57GdOQ3Lnyq357NXi6P4K9m7ZmaK%2B54FACKLTLdeQg6yWLlyduaQ8BkQ0bywA%3D%3D",
        "AMSTATE": "BBAG=256&CID=6eef1729d2b6ebe9&RENAMERULENS=EASI-True--HOTMAIL-True--LIVE-True&NewMN=&UserNameQs=&SESSIONID=5efc8eee-acea-43f3-9543-6f1f19150aea",
        "ANON": "A=1AAD4B1E611E32F23AB38286FFFFFFFF&E=1581&W=2",
        "CkTst": "MX1532998932538",
        "MH": "MSFT",
        "MSCC": "1532961114",
        "MSPAuth": "3RBCa263TG!Q4SPHaHEpESCK2MddKdsHNeoJaZNE0UUXuLKuk**ig5aQWxKB4W4BUeSeoKlnVVnqm61oGgH96wojzROBdOAhaUOKvjBpBzcTRTTEbiLiMx0djU*pNHJgLcP41xs*gdmhw$",
        "MSPProf": "3DIIkMudFFREn66VH0NySvqERzICdZzIH52p1BYB4kukC2awOUcNiasPm3u8iUJYf8fZBUI4ZIKmpPzlVf*A0uqe3GNV6X*eecQLDPWLgloVyaU2IKdq9jT5NPx6x9jUIS943CtGXrd1P6D04xPbQ2Dw$$",
        "MUID": "07462D7D021E6D2B18BF2144061E6E38",
        "NAP": "V=1.9&E=1527&C=UhMIHp-9yDGKE9saUeODr_M-INN7-Vysikfz9vBiTrQL5XaBfRrXzg&W=2",
        "PPLState": "1",
        "TOptOut": "1",
        "WLSSC": "EgAXAgMAAAAEgAAADAABo2cs4ZiBIfGtz7em/irc/M+lW3ngeTMmwL9YsueElkk6uomD+4AfzoT+PXlkYmi+vaYX9sP/6s/Ru8IhHBUGCD3zQhqhNylbJEyWw/bE63abGRR4CaQcc4AYTWsPXZeF32qGFbcsERuztOFZWSKNIg8L03A6syeMJBH+zHJMYa/gAOZyzQvXhIhYZGYJQjtuPlzBJf8risMy+Xw2MLkGZ2TnsyQPd3u2REKPXA550EApzFwNDegBSQdsQqNxfL07Uw1YbN7IEIaCSeCERrRPWZxpgk/BDxAfZLRRVMCfEUGldViknno2h8///Hm+1z4LLf8/qfPwVovH+Qwx32jJyQYBeAAGAf5/AwAVOCYY9rRfW++0X1sQJwAAoBCgABgPAHhreUBvdXRsb29rLmF0AFMAABt4a3klb3V0bG9vay5hdEBwYXNzcG9ydC5jb20AAAABVVMAAAAAAAAMBwIAAIb4VUAABkMABUthaXlhAAVYaW9uZwAAAAAAAAAAAAAAAAAAAAAAANK26+lu7xcpAAD2tF9b71vWWwAAAAAAAAAAAAAAAA8AMzUuMjI5LjIyMS4xMDIABAEAAAAAAAAAAAAAAAAQBAAAAAAAAAAAAAAAAAAAAGIxl1q30EaWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAw==",
        "amsc": "UcN/D3VTIlhYfkUiWp1N4EXZoF+qNaRqD40wEEs1LQ6ycjHd1m//dDTnMd2rtNme87P9SXc+8FhxgX4H7g7WUfcrdQ4lNpzplNcm4f1Ft9aAD9AO/IYj4zOMLJZEIbPhoC0x9dC+pKf5bbzNtS5yOCKcE014zYU3RaUsjxp2iSWN2heFnIfu9DJcx4eEQ732sLrvhSuYd9qWHroOGZsfst0WJJyqHMKRtWqv2ZrB+mMnWLiBmqsQQqi5hEweE7GN:2:3c",
        "mkt": "en-US",
        "mkt1": "en-US",
        "optimizelyEndUserId": "oeu1532997911461r0.6460919936895175",
        "rewardsinfo": "en-us%3Ben-us%3Brewards",
        "wlidperf": "FR=L&ST=1532997987258"
    },
)
    resultStr = req.text
    # print(resultStr)
    if "already" in resultStr:
        print(" already have!!!: " + addressName)
        time.sleep(5)
    else:
        print(" available! : " + addressName)
        break