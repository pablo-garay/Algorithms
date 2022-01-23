from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):  # Time: O(n) (sliding window) - optimal as need to traverse whole string in worst case. Space: O(|s|)
        d = defaultdict(list)
        ans = k + 1 if k < len(s) else len(s)

        for i in xrange(len(s)):
            d[s[i]].append(i)

        for letter in d.keys():
            left = 0; right = left + 1

            positions = d[letter]
            while left < len(positions):
                while right < len(positions):
                    if positions[right] - positions[left] - 1 - (right - left - 1) > k:  # k not sufficient to fill the gap
                        break
                    else:
                        k2 = k - (positions[right] - positions[left] - 1) + (right - left - 1)
                        rest = min(k2, (positions[left] - 0) + (len(s) - 1 - positions[right]))
                        ans = max(ans, positions[right] - positions[left] + 1 + rest)

                        right += 1
                left += 1

        return ans


print Solution().characterReplacement(s = "ABAB", k = 2)
print Solution().characterReplacement(s = "AABABBA", k = 1)
print Solution().characterReplacement(s="ABBB", k=2)
print Solution().characterReplacement(s="ABBBA", k=2)
print Solution().characterReplacement("CUTQSTZSZBMBCVMQLHTHCEQCICXEKJPYEPKLUJRCUULAZRAVPVKNYQIMMYTTMRCZVSXWNFUWXEOVWQMMKMWVFRBKTVISHXUYFXYKIJUCFUMMJZMPAFDDHBALJZGWQMSDXSLYLJHDHSQXSVEEYKFQMMPRRIESRHVJBLAVLYWMTWUTMULMKRNGYBTXBLEGLTWCFEGGIQMJCXEWNKCKBLOVQOXAKBUJIWXYNVCNVGRJKPCSJPZVPUXKVVEJPUWEQPBQKGJBKRKEIQWNGHWDSRUXURWCTMRUFBOWDNPJWYKPKGUXECVQNVKNGDFRSCGJKYVCRAMHHUPTGITNPIDORQIARYILWKBKUVUBUOZFSKBUWLGOWCNMCILCMLHEFPQBMRYTMIZONXRBKXPUGAMMWXDMKDCAWOXRVQNUEAPXOFWFNSVTQCWMDFALZKOFIMKQDICYFWLDILBSPGXTELZROWSOBHNDZMOBJHFUTPUZLVYOUECDWKBZDJTJIPJHAHOFECLMPGHJSDFMENLRAJMWAQQOTTAGYQFRKNMPJVAFUPFRSZGKHCAGGBQCMCCFVOPYQYYCAQIOUBEKODXUAASRLGCHFVWURZHLSZZSISJGHSEEKKTJETSYSXTRHUAQGTLRYGQPVHCKKUUDNHNWRPOGWDSQFBRVAAPEUYFTBBDNHABKOVVLCGMTFIENQWFSWHIQDDTRBLJBYBRHYEQWETUGJWWQNJYWIBWBNWUSPFQKFFDNRZXPZALQNDXIOJWYUIKGWKUHYPMMZOIJSEBOJFOXYVQRZIDNXCZWEDVFAYYEXDYGUHCSCANKJRELKPWWHPMBBOZNJDDZAHMTDYZNVHMAYZVBRDSSIFYOTKUZXGFVZMURMPANIWSLNKYXSYCAKFFKAZPTGADMVSAPRCPMEJKLNWBUKAFKVFEMTCWIRAKSCMKNLTCFUIUTZDOYRIDXHOTQEZAERTFWXVNKSCTVGKAXRTWLKXYSMEWRRVYLHEGLWSW", 100)
print Solution().characterReplacement("CUTQSTZSZBMBCVMQLHTHCEQCICXEKJPYEPKLUJRCUULAZRAVPVKNYQIMMYTTMRCZVSXWNFUWXEOVWQMMKMWVFRBKTVISHXUYFXYKIJUCFUMMJZMPAFDDHBALJZGWQMSDXSLYLJHDHSQXSVEEYKFQMMPRRIESRHVJBLAVLYWMTWUTMULMKRNGYBTXBLEGLTWCFEGGIQMJCXEWNKCKBLOVQOXAKBUJIWXYNVCNVGRJKPCSJPZVPUXKVVEJPUWEQPBQKGJBKRKEIQWNGHWDSRUXURWCTMRUFBOWDNPJWYKPKGUXECVQNVKNGDFRSCGJKYVCRAMHHUPTGITNPIDORQIARYILWKBKUVUBUOZFSKBUWLGOWCNMCILCMLHEFPQBMRYTMIZONXRBKXPUGAMMWXDMKDCAWOXRVQNUEAPXOFWFNSVTQCWMDFALZKOFIMKQDICYFWLDILBSPGXTELZROWSOBHNDZMOBJHFUTPUZLVYOUECDWKBZDJTJIPJHAHOFECLMPGHJSDFMENLRAJMWAQQOTTAGYQFRKNMPJVAFUPFRSZGKHCAGGBQCMCCFVOPYQYYCAQIOUBEKODXUAASRLGCHFVWURZHLSZZSISJGHSEEKKTJETSYSXTRHUAQGTLRYGQPVHCKKUUDNHNWRPOGWDSQFBRVAAPEUYFTBBDNHABKOVVLCGMTFIENQWFSWHIQDDTRBLJBYBRHYEQWETUGJWWQNJYWIBWBNWUSPFQKFFDNRZXPZALQNDXIOJWYUIKGWKUHYPMMZOIJSEBOJFOXYVQRZIDNXCZWEDVFAYYEXDYGUHCSCANKJRELKPWWHPMBBOZNJDDZAHMTDYZNVHMAYZVBRDSSIFYOTKUZXGFVZMURMPANIWSLNKYXSYCAKFFKAZPTGADMVSAPRCPMEJKLNWBUKAFKVFEMTCWIRAKSCMKNLTCFUIUTZDOYRIDXHOTQEZAERTFWXVNKSCTVGKAXRTWLKXYSMEWRRVYLHEGLWSWBRGBASLRRTYYHKXTMAKGZKPSZEOCMFWFNULIFJWXOUMXPPCVRRIYLEURKJTVQIKFYCGPLTDCFINDZSNIGFZQGOWDLRTCCYEHKXINCUYIPXQEPABLMGVNHZHOSWOCYPUJIJMVSWFYSOFRITVKSKDRHCNSTLCWZLRLYNDJVPANHXDWYKLGANHAVFDGMIZVARBDGMMESZZUIUTAYOMLKBMAIJDWVAVRURUEOHXWZGLJFWVUCPBNNDMDBGYJBQPPTHITPHWKHTUVDRJMCQDPRXXHYNQXDVYQRPSHRBZCYTUWYTFRCWIBDDOBDCNWGXUEPSEZCEVZLYHXAAOGUEILKSVWHAFLAAKXAWVBFHLJYNXNRCKHAJCLTZYPBJPFABUBQTBYXHGUZHWZJJSHWAXDOMIQZWUUXYYZQVGNIQPREBELTWDUQJJUEKIAJTUAZDXBDEHSRQYXHOXYEXGKYDMBJKJIMPEEFQRRARUDEPANMEROXGHTVKTOJFZDTGZMJLEPIXSKCWYEMERBWIDMIKFXRJUDVNRNSOCXEDAUFXFRZRTZHTKWCQHSNBRGBKHUSYIYLEAIOCIUMWRYLQXAFXRRJKLEUNQXQUOGGDQRCGKBWHSJHWYUYSWUGKIHCGPNBCOTHWIDCZOVVTBUURUSZTCJRAWTNFEQMLVBPVXSTUGZXCBKAZCCPLPGKSHUUGRGWQAAWURSUXPMZCZBPDJZVGVZPOCXOFYWMMFOCQUQGHBMHIZXEJFXXTNSNCJYHJXLLAEQFKCMQLQTIVESDRDOMJIPXXAIGXEULGRZZAMUNBHBVYJGKCLVBFTCAOBFUXOHOECQWBIGYVJGJISMPNXMKURJSMKOLUGTJJPLTZTRRVGSLWCBPOXFTJQXJJWSDMUSOZXIABESOWKYHHORVNIEOVGPDMHFSWWVGGVPSWGHDQHLDBRQNEKJXVNJKPUYAFGVJLBXADKSJWHJYEOPWDVDZWCUXBMMKAWKGJZZEMDODAWDLHHUOSDQCDCXCYGAOIDROWMMVSPNCMRBBWFMXGJEETLXIHJJSUURIRRMPGRPYINRIJGKSHKPWEZDALQEVJIGICMONLBXIPHQFJPMFMCYMWFADFKJNLZMMHCINCOGBBVKITFHENTZZQTDNWGDOPJUNHJZEJIOZXFBDPIPTDYFCUQDBCPSNUKKLVFIZTUZWPDBGXCHUOACWEBUQQNMYNCRNVKJUEDUJKYXOHWSFQWGBQHPTOWRITQALXROVQZWIOILGDXEMKZIMGRHDLGNFUMOWWQJVQIOKRRPRVULSSYGJVGTVWYNKCCYQJNAMXGVRMMCPULLSIDPQQMGMFSQWFBPTQFCSZXZBZQLZEEAQBYLFWQHKVWAWUWUYMFYQLVBWNBYFEXOFTUMOVDJYEWYORUWQWDFLNGMNHIPJLFTRFAGFRZHCOZTYHDFFRIKYRKCJOPWPUSDWLRUTKWTXTMECNBXQAVGQTXQHNYHUDMAUSYJUMAAPJUMDIJDAYBWYFHOKVWZQYWYYEQBOMARSFHEZZDYYMONCVIDGFIRDJJLTNCTPIAXJMKMBQSXNPYZPURGWYSHXWVZLOBKWNINJJYOHKWMGKNFQBQIPISJDIOJPQBXTVFEMIRSZAPEITGIFEJITKPSMFAEJFWRJCWOXMKDPVVCDPQWFTRCIOYBWALWRRWWGKXURBDRGVUCKIFTJODJQDKHCOHOFLSNLFAMWBXYZASGCBFZFGFRQVJGRDTKJKTABPPYPHWZKWRLCFKJDEABOSIJNVBBELNBMYJUKZSJBNHHXUCMAXGLYSJDBGJCHTYKJQCVPPJVNSCHRFRUEZOHGKVQLVYKENZHPIODXFTJUVRFCLQPPGAFNMZJCLGDTZCWRVNERBASFLEAJFEYGIRLFWAFSLSUXVQJUOSSYHEVVHZYMRQFDRVQVMGABPTFSFJDGGYZRGHWAQTJCYNRHDGOOCTVGHLUOZWVOJBLSQPDSQBBRGQADDQQKBOFBRUADIYPPOYPVDWUBRTUTPTMDLSFDUVWPEECKFHYXDUPVLNPPNKBSYYOFFQKEJKJMBUQYJSRUJHITJOQGMSBIHFXQOQIFQRLQDDCSOSPUOEZBLJSJZNEWNFOAOKHEEKXDCYITHYSXOYMEMNZOCAZBGEFZCWAPIZXYDKSUJHTQPGPHYPDOWEBNODTLLMYOGGUSNKKKFVMVAGDPZRJKJRRQABJZUQKOUSBIGBJAEYFYWZMPNAHQJPZVUNVUACTHACPECEBJMVVIRXHHDBUPQUWRXICTYHLSBVRCLFPMLQVLQJDDZPKZYNLQXZZIETGYBURDFXPDAABRWDCCOTYPVPFUWNRGAGLXIZLEEHSNPIVSNRSFVFRIGIKOMLUMQEVJKEEEQUAQTRSJDAXPFYMDVNOLSICQDTYKBYPQYODWREMAUZZAPHPOCBAJRTELEYGKCANGNTMKTOODJMDOHLLYDILSFMPJNCBKXSCOEQJREWSRZWIKJUIAEIIKWCDAWRDRFLXQVYMIZLKDKSSIJGJZYOKIZXWOFNHKMVUTZALRZMBSKADAZTBSRRCWJEFPBDZMWRMNERMQPMUKPBJXQKAHJOBBVVMEHAOYHLZMQHOXVIGSRMDWCNBATUSVMBFIDIYWEBWKLKWOVJROPXNDRWKWKDDQENSAGTQKGQBJUWSUKBOIJNVBJGABTOSSMVGQFAPCRGVGUSBRCUVJEMCVUFPKMEXUDSVJBEDGUVNMNBJKEVWVFFSHWOVPNUBWLZYVREWRRVGVYFMXEUIRXPNEIDEEVHJLVHSXGNYWLOCRWQUUPRZNXQEECDSYCTKFEZYXCLUBVTDSWKCFRTHKDKNORMMQNPNSZVSKSCOQTJTSGCCSHAXFLRYSBWCLTZAHCOUEAJGOHRTBVIXSQFECEVPEOKRTXFPGCTVDKDQJIPMLOGFAWGXKWRSSGNLVQIAOKJFXQGVPEIMIKKGVZGKYQXYKAAZLTJDEJXYGVCXPLYVTQQIAZBABDPAKZODIASBJJEGVOJBMKEMQEVWFBKFLZXVNGWFSTGBQMHBRSFJFENSKZJUBQFLWEMBBUQLYFYRMQCMJXPZVULTZALBZHVLCTPRBKVHRGVJDKPRUAVOEHQJCIMWSYIXNTYYTGBAPZJFODZKDYERJSBUPAPPHBNSLYKKAFNQPNZSRHSXCOQPSNWYMXCGFPPGWAPNATEBEDSJFDTZYMKEXNTGJJOZKACFNFVSEECSIOBCMINUIWNLUDSZQRFADMJGWGAOZGWPYXARPYYHPWZCESKNROBWBCSXAMMHHYPWELCPPRPQIFCVNGVXDQHULUPRRQEOMSGESICSRYEHCWECEORJFNUQVJMAOTSJNBWKTMHMKDTAVWFHZYZZIOAIKRVPITZPYSUWDVRLAUPALXXQVYTJTVEFBETLBSZBWAUZVIYUMUVTIMUZQBLMPNVSFWVMTLIFYAHSRIVICTNDZZOZHAXFPSYGHBRYDXAUZEGFMEHNZEJGJDIBHXPVYENHJOHOHDWQVGVJJDGBSITVCZYPLKXZIBHBIQPZNDDUTBYSYKNFYVBWFENYUAAVJDWHMZHIQUBZQBYIZYFKYJSKKLUSFFLMDUIHWOBZQBAZGAIFHPMORCYKUINDJOIKKKCENXJSHZMYOEGLTVBHRJPXYGHUWJSXXMYJSETKWDEDARIQPLWHZXTUGEDSCHSNMOGMZASXNEODTQVSLTVSVQBJWXCSGTCUIAOLGEKSEEFBCFVOPIKOVJONZNRMGZZZAXFOPPLICTFTNSSEFWABMXQPRIGBBUBWSXWTNQMZRYRHROHECVLVBDTLDZWTOWJUCDKPUOZNHTFOYJIALSZDCCNXTUEKXEZRWVLWRJYWCYONNZVLTOGXKWMUYJTGEVRROPFLETSGLWRUWDLPYJAXOTWMKVBPDNESLBOYOSSSFVARDTEXNHCZTVBJRQWWZJDYZKPTZCBPAXSQYUDEKWZVCHDNHUPKSOLWSHDCHXYFVEBDTXISBUCFWPCKXDHUCLTOPFJOSCCOWHYJGRNDWASIFKYECWWBTILDQJTWXNRTKNBPISULXMOFDXVNVFVLIMVHTTSFXUQCPKJPZIJUASYITFIMKVQDZBTYJBFHMYHRHYRMZWUXRBDCLTLZEUGHGNAZHVFOTEOOOKMBSTIPNATUFDWMPLGQSGPEXOJUIFZKOMHCXADOOPCZAFTIDDMLEFSFDMPGFHKNITQNZDQDEUHPYQSBJTXJFIAOONGAQMTRQDTKGWPIXSESRVPFHRMHNHNSNOIIHOOHBYRLYVBHWHSDMYZVNLVKLEEDTGQTTXDYANXZKXJZRNSTUPOCDWJILNVVDDSCTJSZJKDCEUJRETFTZBBDKXQNNLSXIRVAVSCRBQBQWBVIWPEPTPBTZOYWJNDUUVNYAMZRCKOBAKVPEPDGSMRDQCZEZEHPOXTKGMBOBXDRYJLBGIMFFVNLCLRYWUEFTBHOKZXJANRFUOBNTYSNLTKQSFDTNDOAPLTKSZBSXFJWAUNVPXYIAXXBOCLVTALHYARTBPFSUPILRNNBXFTHFJCRNANYEWYYCZGITRPYSPBPYXSNMZBMXUGWIIBNBUCKMQCCHKLZVPRMPPKMXSBKQVQSJSDGHWVFSJHLCSMQAARRPOPITAHIPJPJITNRQSICWTBVKJCZSVBJWPQJPGELEMLNSHNQIEXIMRQAKYVVNIFSIEIXHCJUBZZPCOLPWGFTHFCUTWBSWDHDUSPHZCUQIMOEXICIOEBRRFPMODZLQNEKEKFBPJTTZHMOMVOAKVYOMBOGWOIVVPUCKHSOEFKDIRQLPRHWIKXRFWXJZWNIJZXPTJARTJQTGEEYSIDKIGXMNQNPPFIJNESULETTHMXJWDOEOBWVGNSXLLBHIGFWKXBZPLQOAZDMVGKEPGREVSNRAVJBXCBWFVPZLDTNXRFCOEMOBOJEEPSABSCOTEVXVFWZNQDVTFYFZCLDIFTJKYBUAFNQJEMPFBLTJGOEFOPQACKREKFCCOOEKRVDQZGPPROJOTJOONCIYKSUOJWZULHYWPMJDPCRXRIKCAAOWWKDARYGVPGZFZBXKZOCQVHUQQAQGKTTDKPAIEYKYETDDJAUQDIPPZKFOLGKNISJUVBMSATGVVZXOMYKFTPTWASRETFOBISTNJWSTFGZXURAUDOOORMQOUNXBFDFWFUDFYMOWUAGZPKZPWCMKBUKORLYZXAMTIRYATQXXXAESNGICMYMXVUWNSUSDGHHZAXJQPTCBVUBWSBUCIXUTJUJIRDRFETQKMMREECNIPGGZHUXWAZAUTFTDXZIKCUCFVXLFBZOOVRYWEFBGQUPJDSDLPLESIBXGZHZFZKXFFEKTJMAJAZSAJXAVBERMTPEFFNRFOCEVPPUVNRIXQQQTCSVQNUWCKHEZBGYJXKMYJCIUTNIXVCAIULWIOUDSHZXZUGJDGNUQBYQPEUEGZISLMPEJJBFBREEXJKZEPEVJSQGMWCJDEAXXPUJJEMMYUPPEKARWYDMFXJXNSZLBKHOCQPIZWVDLWQSLQFAHWSIQQSBJWOCEXDOJBYIXMTLIPWQUXREGJOCSBEOCJETKQSXLGINLDEHHWXKNMEGSDEWGVHRAINVVTYNCOPKHLYPDZWQQQCXGUQXISWMEZNUYTLDFWEHCSCMYODRMAPJAUJSBXUYHAGWIULXKSXYRUYTLEOAJNBPEWIMWPQXUFUGKBWFAKRFRSVXGTZBVZIBDWODYTLGKJMSXHSFKHELYFAJAOPYSNFBQAVELIRWUSGNGVVWYBUWKWRJUNCRCQZJQSJUTKQLLXMWUOHLURQRWKDUVGFMNCDTCJOTNFLEVQWSKKHIILKGUBAWCNJFGSLMTGQADDNZENJQBTYRTVXCJYTFMNXCNUGBTKWOZMLBAJEBCEHOZSSUSYWEGVLDJPHPNEHQDUPRRKIGWJLXBJALUYQQPVTEVREDIHLBXPWWPLZIIPWDBNAIUACHLTPFRUBERZGBRZKSNDFOMFDCHQXEUWRWVHYIRQKDSCCQWMZNEBQSBKHNNYHXSDWPPPSVYAFFSWIRDBEIGNBDILUWMTXAIAAQOUZSSQYUQEGQCDEXPNKDWOSXBFRWQHOXLPNPPQMQFBQQNKGRSLHJJQOECCIRTEGTHIDNZOSEMSUHZCBQGUNUOVJSILDUUIRFONLSWUJDMSZYSPZITJTIDOXEXVHUCVULHDYEGSIZWQFLZVWDNCEXZRDZILLKBUQHUFXIVLAPYGYFTUNAVCUYEHWZWJHQXWWLRPERVMJIQADVNMASOYPQSXITDPCWMEFEJGZUKCCYMPIWHGXVUUQZCAZLXIYIHJUAVTLACTSYESSDFWHDYDHYAPETWKTZVQLOVFYMMCKPGQZGMRFSALGJXXUXLTMOQSYQBAKBJMLXVKTXZXHXYXTRAKRDIONDBZVLCDKBQMPBIVXLXXKNDPTCZFNLINXJIJZZKBNBTMTDNIULDLHSAQSPXZKXDTBKVVCYZKGFNKPPGCWVWLNPJRJKAJAPLJDCVPOHVRUCBMLWGIAJTWBUOZGDRBPCLUWFIWDGMNWONHDISLCUHYYYLGHGQEORYEFGYFRHQBKRKFPICJNMEWTEATTSTYOYLQHLNALECIZMWNBCQMVBWFSPSYCZPVZYXPDNYQWVFRVAWWHTYHWEPIKDHJCUCAREYZKERRCXQKVUKPWGFUJPYQAEFXYQLMCTAGCZHDOBJREYXQCXIBPRUMVJNPCJDBMPQQQUDCENPVLMYJPBBXZRLEJXECCIIWHONWQPDKYRWCKLFMVLPFXCSNERJLOEWHUGFEOGNZWBHAXRKDGGVTQBWGYEIFRJQBFNKGSQECQJVEZXOZRDJNTCYYEOFPSEYKJAMJTXQUFRARYDGZCNRYSIUNGBZXRAZOXFZVMEEEQJYLGWMYRIRVZDFOHZMPQPYRQNHLEPVLHXNUNWKAHSOWLATKJCDZDPEWUEWTKQMAZSJPVOQCUBJRERXRRJOGWHVZJUJXXJZMLCSLPEPMBGGULNYGCTPPDSERBNUAAZRKUYXRCIWLQZDREJEPKPPAVLOQDJNXCAIQWDAVCMOQRHOWTRPHONBVRMIQAZKLPEPDYCZAGCWETPIECCITHJGDWOHYCMJLJVXFBXJNWSOAOXBWBCAIOLGHAGNWOEEOMXHDVWVSFKFZTQISTBFXVCERUAOEUQZMGBJMODTZPTNHKGYYRPGRAMNDMACMLBKZDHMVNKKGCSJVMQOGDOLCWYYDKWWCBPPVRSVEKDUUDOIVWWFMBIAUDGDIWOGAMXVOOSQOOVAOVNUYNYSLNYRIVBBTBMPUXUCORMRMBYVDDGTPOWZRFYLVRJDWYMGDYFPTPEJSUFNITSPSBCQZHTCUSMZFDTSSNBGHPQHRWCRMATJIPJCRPVGIOCWFNVOCYYHEUQEADNUHRWNPDEKWPOHJGLLWNJKCWJJGHXROZSEWQGRYTIFANKGCQNTUJDKTIMDIPRYCVJEYHAHNLBXKXYMNBLUNUNPSXQCHWKFBBPSQCJNPZGHGEQJICGDMGQOMCXQXFGXACNPXCYBTJTVJYJEQAYCGXSHUONCNGIYWOFIBFEWWECBLEVYQMXZEALYMIFLSIZCBKOJAOSFKESVEEFWMMWMKCDZVGOLGGSUFLHEVFJBSEOQTORDWCUNKYMOUMFOKKVZTWLTAYCCFXEYYGXDIHFVIUKYJTBNZUYDOPJGEZMUPCPJXLMOSXTBGCVMMCUOUKCZQEKUNOQPCDLZJSLBOENWKDCYKFWYNOCTFQAGXRLCJJFFROJUGGLZKIBGXHIAMIYRBWVUYSSJCMFVBQSHJOMXOFCMTTDIUPYRMGDRACBPQZCHXKZOWUOQRWZTGDEBILBMNGEAJWRXMUDRUODXGSUCCNMUPYWABYZZBUZOPRGUXYFBZYHIQLOCTRANAQGCRFATDBADZMSYFJHCMZJEJZLXLIZVQTDLSJNIOXNTXNILOSEEFVQQZYGQUGZCUNHEEEPXYPHQJUHHMKUAMYHXWROSTAEYSHGXIJKAOXIESLOBICIRZMVAOKEFTJRXGOOHHGRFEWVXMSEHPTPUKUQZCOWFQFVAIOAITOVYQSZNRLTZSNOKCWIDNWMICTQUGJDJXMUJLNIGVBPCVAROSANVUPWWHCFVDSUVVFDBXQBVWBALEGBQOGIKKIHNWWUTDHBGEZUMEVHBTRSAKAYGYOSFEKPZRUBZQWATYHMSDBOCUZTMJEULVROFNNHXAEOGKHVFNEUISWISTUDLAOWEFXIIFEIXPWSJZAKXPSJFCJTBCDVSTAGGCAKECUQPIMCDXBGUAATNDTKDVVQPLMQQGOCWSEDNNACJCHLGDJOJZUANACMTURVPONNOHRIOSBGCKHTYNVCVBVNXLDOLOFFIGVKXQVUNHDBUGPNTBFODMHHNDUGPTRFSZPFRQUDMUHVRKXDTZNDHJLCMMDKOXROGQKQPWLSCVZMUHOLNOWFBZYAPBMCDXAZEMJNWLUFNJOZQHWHSEMZEUQZBEJTDGERQGTACWPWWIDKJMBFDZCYTCZLDDGVPVJAFAJODLFJQMKTNCHOZFEZJUFIQMDKUZKABARZTGYAJDUMKLCOCKOAGLIEHHRQSTITNCYTCXMNHZJWEFPJDROKIQULNMMMLTJNCOCHSTTOHORDAALCSDRNRWFSVAKHLBVJTTXVBDKRWYFMJNYQQKIBAMLITRKMHEZNFBIWDWVBOHSRODSLOBCFCGXHDCEGMOTAFOFWUTIOFIKJLDQKFBXDLNZWCMJTFEZONCKOURMZURYSQWYXWMSNXSXYBRYYKBHFUENSZGYEICSJNXSMBOOJAHWXRCKCRKOPRZWNXMUMEVBNJYKDAHPSTUUNCQCHRUYWZULAWNSZMGZCNZIGHPBXSOEGSALRIYXFPFFGBCIZUCMFZUEFGAYQKBQJRQHJJHCGKHFCBNBRAISTMUHSKQSXBDBLAFZRTVOSKLGLBKOLMYLZTEDRZOARTZVVSWRVXSVMZXGIAEDDDKPSPPENZGDIK", 100)
print Solution().characterReplacement("ABCDE", 1)