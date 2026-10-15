"""Build index.html for the 'anthropology of the future' reading list.

Template: the head (CSS tokens and parts) of urban-memory-reading-list/index.html,
which follows the esse-sense report base (/esrep). Only the content changes.
Bibliographic data and citation counts: OpenAlex, 2026-10-16.
Summaries are written in Japanese from the abstract (basis=要旨) or, where
OpenAlex has no usable abstract, from the bibliography and secondary accounts (basis=紹介).
"""
import html, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = ROOT.parent / "urban-memory-reading-list" / "index.html"
OUT = ROOT / "index.html"
DATE = "2026-10-16"

A = [
 dict(au="Joel Robbins", year=2013, src="Journal of the Royal Anthropological Institute 19(3)", cites="1,227", anth=True, oa=False, basis="要旨",
  url="https://doi.org/10.1111/1467-9655.12044",
  title="Beyond the suffering subject: toward an anthropology of the good",
  lead="「苦しむ主体」の人類学の先に、「善」の人類学を構想する。",
  s="1980年代、人類学は自分たちとは根本的に異なる「他者」の社会を研究の中心に置くことをやめた。では何がその代わりになったのか。ロビンズは、それが「苦しむ主体」――暴力や貧困、トラウマにさらされた人々――だったと論じる。この転換は他者の人類学が抱えた問題を解いたが、他者との違いから自分たちの社会を問い直すという批判の力は失われた。そこで著者は、人々が何を善いと考え、どんな生き方を目指して生きているかを捉える「善の人類学」への移行を提案する。未来や希望を人類学の主題にする近年の流れを方向づけた論文として広く参照されている。"),
 dict(au="Vincanne Adams, Michelle Murphy, Adele E. Clarke", year=2009, src="Subjectivity 28", cites="1,084", anth=True, oa=True, basis="紹介",
  url="https://doi.org/10.1057/sub.2009.18",
  title="Anticipation: Technoscience, life, affect, temporality",
  lead="未来を先取りして今を組み替える「予期」を、現代の統治と感情の様式として捉える。",
  s="医療、科学技術、安全保障などの領域では、起こりうる未来を計算し、それに備えて現在の行動を組み直すことが当たり前になっている。著者らはこの「予期（anticipation）」を、単なる予測ではなく、人々の生き方や感情、身体を方向づける現代の時間の体制として捉える。予期は不確かさを行動の根拠に変え、人々に未来への準備を絶えず求める。その結果、現在は未来の名のもとに組み替えられ続ける。未来がどのように現在を支配し、どんな感情（不安や希望）を伴って生きられるのかを問う研究の出発点として、人類学と科学技術社会論で広く引用されている。要旨は未入手で、書誌と二次的な紹介に基づく。"),
 dict(au="Nancy D. Munn", year=1992, src="Annual Review of Anthropology 21", cites="1,039", anth=True, oa=False, basis="要旨",
  url="https://doi.org/10.1146/annurev.an.21.100192.000521",
  title="The Cultural Anthropology of Time: A Critical Essay",
  lead="人類学の時間研究を総覧し、時間を社会的な実践がつくり出すものとして捉え直す。",
  s="時間は社会生活のあらゆる場面に入り込んでいるため、その研究も際限なく広がる。マンはそれをボルヘスの『砂の本』にたとえながら、人類学の時間研究を批判的に総覧する。時間を社会が持つ固定した「時間観念」として記述するのではなく、人々が日々の実践を通じて過去・現在・未来を結びつけ、時間をつくり出していく過程として捉える視点を示した。記憶と予期、暦や周期、権力と時間の管理といった論点が整理され、未来をめぐる人類学が拠って立つ時間論の基礎になっている。時間研究の入口として、まず読まれる総説である。"),
 dict(au="Jane I. Guyer", year=2007, src="American Ethnologist 34(3)", cites="832", anth=True, oa=False, basis="要旨",
  url="https://doi.org/10.1525/ae.2007.34.3.409",
  title="Prophecy and the near future: Thoughts on macroeconomic, evangelical, and punctuated time",
  lead="「近い未来」が語られなくなり、目先の対応と遠い終末に二分された時間を描く。",
  s="1950〜60年代のイギリスから眺めると、アメリカの公共の時間感覚は大きく変わった、とガイヤーは指摘する。かつては数年先の「近い未来」について筋道立てて考えることが重視されたが、いまは目の前の状況への対応と、ごく長期の地平への志向とに分かれている。この変化はマクロ経済学の語り口に最もはっきり現れ、福音派の終末観とも驚くほど響き合う。近い未来が空洞化した後、そこを埋めているのは、借金の返済日程のような日付で区切られた「区切られた時間」だと著者は論じる。人々が近い未来をどう生きられなくなったかを問う論文として、未来の人類学の古典になっている。"),
 dict(au="Sherry B. Ortner", year=2016, src="HAU: Journal of Ethnographic Theory 6(1)", cites="720", anth=True, oa=False, basis="要旨",
  url="https://doi.org/10.14318/hau6.1.004",
  title="Dark anthropology and its others",
  lead="権力と抑圧を描く「暗い人類学」と、それに応える善・希望・抵抗の研究を見渡す。",
  s="オートナーは1980年代以降の人類学の流れを、新自由主義の広がりを背景に整理する。まず、権力・支配・不平等・抑圧という社会の厳しい側面と、それが人々に生む抑うつや絶望を描く研究を「暗い人類学」と名づける。次に、それへの応答として現れた「善の人類学」――よい暮らし、幸福、道徳や倫理の研究――を取り上げる。さらに、批判・抵抗・社会運動を扱う研究を、もう一つの善の人類学として位置づける。未来や希望を人類学で論じるとき、その議論が学問のどんな流れの中にあるのかを知るための見取り図になる。"),
 dict(au="Laura Bear", year=2014, src="Journal of the Royal Anthropological Institute 20(S1)", cites="409", anth=True, oa=True, basis="要旨",
  url="https://doi.org/10.1111/1467-9655.12091",
  title="Doubt, conflict, mediation: the anthropology of modern time",
  lead="資本主義の抽象的な時間と、生きられる具体的な時間とのずれを人類学の主題にする。",
  s="グローバル化や新自由主義の時間がしきりに論じられる一方で、「近代の時間」そのものの人類学はまだ手薄だ、とベアは論じる。近代の時間の中心には、価値の普遍的な尺度として働く資本主義の抽象的な時間の計り方があるが、それはつねに人々が経験する具体的な時間と衝突する。生活の規律はキリスト教の実践から生まれながら世俗的・普遍的なものとされ、科学技術は人間の時間を人間以外のリズムに結びつける。こうした衝突と、それを人々がどう媒介し調停しているかを捉えることが、未来をめぐる人々の営みを理解する鍵になる。特集号の序論として書かれた理論論文である。"),
 dict(au="Vincent Crapanzano", year=2003, src="Cultural Anthropology 18(1)", cites="306", anth=True, oa=True, basis="紹介",
  url="https://doi.org/10.1525/can.2003.18.1.3",
  title="Reflections on Hope as a Category of Social and Psychological Analysis",
  lead="「希望」を、社会と心を分析するための概念として正面から取り上げる。",
  s="希望は日常的にも学問的にも頻繁に使われる語だが、分析のための概念として吟味されることは少なかった。クラパンザーノは、希望を欲望や期待、待つこととの関係の中で検討し、希望がどんな主体のあり方や受け身の姿勢と結びつくのか、言語や文化によってどう異なるのかを考える。希望は個人の内面の感情であるだけでなく、社会の中で形づくられ、人々の行為を方向づけたり、逆に行為を先送りさせたりするものとして捉えられる。のちの宮崎広和らの希望の人類学が応答する出発点となった論文である。要旨は未入手で、書誌と二次的な紹介に基づく。"),
 dict(au="宮崎広和（Hirokazu Miyazaki）", year=2006, src="Cultural Anthropology 21(2)", cites="291", anth=True, oa=True, basis="要旨",
  url="https://doi.org/10.1525/can.2006.21.2.147",
  title="Economy of Dreams: Hope in Global Capitalism and Its Critiques",
  lead="市場の参加者と資本主義の批判者を、「希望の方法」という共通の地平に並べる。",
  s="クラパンザーノが希望を社会分析の概念として取り上げるよう呼びかけたことに、宮崎は応答する。著者は、新自由主義の改革のもとで自分たちの知識を組み直そうとする東京の金融市場の参加者たちと、資本主義を批判する学者たちが批判の仕方を組み直そうとする努力とを並べて検討する。どちらも、知識の向きを未来へと組み直す「希望の方法」を共有しているが、その組み直しがどこへ向かうかについての見方は対照的である。希望を、知識の種類をまたいで共通性と違いが見える場として捉えた論文で、日本人研究者による希望の人類学の代表作である。"),
 dict(au="Henrik Vigh", year=2009, src="Ethnos 74(1)", cites="216", anth=True, oa=False, basis="要旨",
  url="https://doi.org/10.1080/00141840902751220",
  title="Wayward Migration: On Imagined Futures and Technological Voids",
  lead="移住を夢見る若者たちが思い描く「よそにある未来」を民族誌で描く。",
  s="西アフリカの小国ギニアビサウの首都ビサウで、ヨーロッパへの移住を目指す若い男性たちを対象に行った現地調査に基づく論文である。若者たちは、衰退と破壊が刻まれた自分たちの都市を、平和と繁栄と進歩があるとされる「よそ」と対比して捉えている。その視点から見える世界は、社会・政治・経済の過程を思いどおりにできる程度が場所によって大きく異なる、いくつもの領域に分かれている。著者は、こうして想像された世界の秩序が、若い移住者たちの行動と戦略にどんな影響を与えるのかを追う。未来が想像の中でどのように場所と結びつくかを示す研究である。"),
 dict(au="Morten Nielsen", year=2011, src="Anthropological Theory 11(4)", cites="158", anth=True, oa=False, basis="要旨",
  url="https://doi.org/10.1177/1463499611423871",
  title="Futures within: Reversible time and house-building in Maputo, Mozambique",
  lead="完成しない家を建て続ける人々から、直線的でない未来の時間を考える。",
  s="未来に向けた行動は、現在から時系列で隔てられた未来に導かれているとは限らない、とニールセンは論じる。モザンビークの首都マプト郊外で家を建てる人々は、自分たちの家は決して完成しないと語る。それでも彼らは、結末が失敗に終わりうることをあらかじめ思い描きながら、建てることを続けていく。著者はこの実践を手がかりに、異なる時間が重なり合って直線的な尺度では測れない持続をつくること、そして結果と思われていたものが原因として現れる「反転する時間」を描き出す。予期の行為を、未来から現在へと向かう時間の中で捉え直す理論的な民族誌である。"),
]
A_RES = [
 ("Zigon（2009）", "Hope dies last: two aspects of hope in contemporary Moscow", "Anthropological Theory・被引用109"),
 ("Mathews &amp; Barnes（2016）", "Prognosis: visions of environmental futures", "JRAI・被引用100・全文公開"),
 ("Ringel（2016）", "Beyond temporality: notes on the anthropology of time from a shrinking fieldsite", "Anthropological Theory・被引用95・全文公開"),
 ("Anderson（2010）", "Preemption, precaution, preparedness: anticipatory action and future geographies", "Progress in Human Geography・被引用1,206（地理学）"),
 ("Beckert（2013）", "Imagined futures: fictional expectations in the economy", "Theory and Society・被引用551（社会学）"),
]
A_BOOKS = ["Fabian『Time and the Other』（1983）", "宮崎広和『The Method of Hope』（2004）", "Appadurai『The Future as Cultural Fact』（2013）",
           "Bryant &amp; Knight『The Anthropology of the Future』（2019）", "Escobar『Designs for the Pluriverse』（2018）"]

B = [
 dict(au="Mary Uhl-Bien", year=2006, src="The Leadership Quarterly 17(6)", cites="1,963", grp="対話", oa=False, basis="紹介",
  url="https://doi.org/10.1016/j.leaqua.2006.10.007",
  title="Relational Leadership Theory: Exploring the social processes of leadership and organizing",
  lead="リーダーシップを個人の資質でなく、関係のなかで生まれる過程として捉える。",
  s="リーダーシップ研究の多くは、リーダーという個人の資質や行動、リーダーと部下という二者の関係に注目してきた。ウール＝ビエンはこれを「実体」の見方と呼び、それとは別に、リーダーシップを人々の関わり合いの中で社会的に構成されていく過程として捉える「関係」の見方を整理する。そのうえで両者を包む枠組みとして「関係的リーダーシップ理論」を提案し、組織の中でリーダーシップがどのような社会的な力学を通じて立ち現れるかを研究する道を示した。対話や先住民の共同体的なリーダーシップを考えるときに、個人中心のモデルから離れる理論的な足場になる。要旨は未入手で、書誌と二次的な紹介に基づく。"),
 dict(au="Cheryl Bartlett, Murdena Marshall, Albert Marshall", year=2012, src="Journal of Environmental Studies and Sciences 2(4)", cites="1,176", grp="先住民の知恵", oa=False, basis="紹介",
  url="https://doi.org/10.1007/s13412-012-0086-8",
  title="Two-Eyed Seeing and other lessons learned within a co-learning journey of bringing together indigenous and mainstream knowledges and ways of knowing",
  lead="先住民の知と西洋の科学を「両目で見る」考え方を、共同の学びの経験から語る。",
  s="カナダ東部のミクマク族の長老アルバート・マーシャルが示した「二つの目で見る（Two-Eyed Seeing）」という考え方を中心にした論文である。片方の目で先住民の知と知り方の強みを、もう片方の目で西洋の科学の強みを見て、両方の目を合わせて使うことを学ぶ、という指針である。著者らは、ケープブレトン大学で先住民の知と主流の科学をともに教える「統合科学」の取り組みを長年続けてきた経験から、知の伝統どうしが対等に学び合うための教訓をまとめる。異なる知を束ねて共同体を導く、先住民のリーダーシップの考え方を知るうえで最も引用される論文である。要旨は未入手で、書誌と二次的な紹介に基づく。"),
 dict(au="Kyle Powys Whyte", year=2017, src="English Language Notes 55(1-2)", cites="1,074", grp="先住民未来学", oa=False, basis="紹介",
  url="https://doi.org/10.1215/00138282-55.1-2.153",
  title="Indigenous Climate Change Studies: Indigenizing Futures, Decolonizing the Anthropocene",
  lead="先住民にとって気候変動は「これから来る危機」ではなく、すでに経験してきた変化だと示す。",
  s="ポタワトミ族の市民である哲学者ホワイトは、気候変動を先住民の視点から論じる。植民地化によって土地や暮らし、生態系との関係をすでに大きく変えられてきた先住民にとって、気候変動は未知の未来の危機というより、繰り返されてきた環境の変化の延長にある。著者は、先住民の気候変動研究が、未来を先住民自身の関係と責任の中で描き直すこと（未来の先住民化）と、「人新世」という語りが持つ植民地的な前提を問い直すこと（人新世の脱植民地化）を同時に進めていると論じる。先住民未来学の議論を、気候変動と結びつけて読むための基本文献である。要旨は未入手で、書誌と二次的な紹介に基づく。"),
 dict(au="Edgar H. Schein", year=1993, src="Organizational Dynamics 22(2)", cites="880", grp="対話", oa=False, basis="紹介",
  url="https://doi.org/10.1016/0090-2616(93)90052-3",
  title="On dialogue, culture, and organizational learning",
  lead="組織が学ぶための土台として、対話を位置づける。",
  s="組織文化論で知られるシャインが、物理学者デヴィッド・ボームの対話論を手がかりに、組織学習と対話の関係を論じた論文である。組織の中には、現場の担い手、技術者、経営層など、前提や言葉の使い方が異なる複数の下位文化があり、それが互いの理解を妨げる。著者は、結論を急いで議論するのではなく、自分の前提をいったん脇に置いて、互いの考えがどこから来るのかに耳を傾ける対話こそが、組織が学ぶための土台になると説く。対話を、リーダーが組織の文化を変えていくための実践として位置づけた点で、対話とリーダーシップを結ぶ古典となっている。要旨は未入手で、書誌と二次的な紹介に基づく。"),
 dict(au="Kyle Powys Whyte", year=2018, src="Environment and Planning E: Nature and Space 1(1-2)", cites="775", grp="先住民未来学", oa=False, basis="要旨",
  url="https://doi.org/10.1177/2514848618777621",
  title="Indigenous science (fiction) for the Anthropocene: Ancestral dystopias and fantasies of climate change crises",
  lead="先祖と子孫との「対話の物語」から、先住民が気候変動に向き合う姿を描く。",
  s="人新世はしばしば、人類を待ち受ける破局の物語、SF のようなディストピアとして描かれる。だがそうした語りは、植民地化による社会の変容をすでに経験してきた先住民の存在を見えなくする、とホワイトは指摘する。先住民の視点からは、現在そのものがすでにディストピアでありうる。そして先住民の気候変動への取り組みは、迫りくる危機への恐れではなく、子孫や先祖との対話的な物語によって動機づけられている。著者は、先住民を救われる側に置く非先住民の物語を批判し、先住民自身が主人公となるSF のような実践に、未来を切り開く力を見る。先住民未来学の中心的な論文である。"),
 dict(au="Ann L. Cunliffe, Matthew Eriksen", year=2011, src="Human Relations 64(11)", cites="594", grp="対話", oa=False, basis="要旨",
  url="https://doi.org/10.1177/0018726711418388",
  title="Relational leadership",
  lead="日々の会話の中で、他者への応答として行われるリーダーシップを描く。",
  s="カンリフとエリクセンは、関係的リーダーシップの理論を、リーダーが日々の中で他者に応答しながら交わす対話の実践として捉え直す。関係的リーダーシップとは、自分がつねに他者との関係の中にあり、それゆえ他者に対して道徳的な責任を負っていると自覚して世界に関わることである。人生がいくつもの声と言葉から成り立っていることを認め、関係の中での対話に身を置くことでもある。著者らはバフチンとリクールの思想と、アメリカの空港保安の責任者たちへの調査をもとにこの考えを示す。日常の何気ない会話の中に、責任あるリーダーシップの新しい可能性を見る視点を与える。"),
 dict(au="William N. Isaacs", year=1993, src="Organizational Dynamics 22(2)", cites="569", grp="対話", oa=False, basis="紹介",
  url="https://doi.org/10.1016/0090-2616(93)90051-2",
  title="Taking flight: Dialogue, collective thinking, and organizational learning",
  lead="対話を、集団で考える力を育てる方法として組織に持ち込む。",
  s="MIT の対話プロジェクトを率いたアイザックスが、ボームの対話論を組織の実践へと応用した論文である。対話は、意見を戦わせて勝ち負けを決める議論とは異なり、参加者が自分たちの思考の前提や習慣そのものに気づき、集団としてともに考える過程として位置づけられる。著者は、安心して前提を問い直せる場（「器」）を整えることの重要性や、対話が混乱を経て創造的な段階へ進んでいく道筋を描き、それが組織の学習を深めると論じる。リーダーの役割を、答えを示すことから、集団で考える場を整えることへと捉え直す手がかりになる。要旨は未入手で、書誌と二次的な紹介に基づく。"),
 dict(au="Chellie Spiller, Edwina Pio, Ljiljana Erakovic, Mānuka Hēnare", year=2011, src="Journal of Business Ethics 104(2)", cites="141", grp="先住民の知恵", oa=False, basis="紹介",
  url="https://doi.org/10.1007/s10551-011-0905-y",
  title="Wise Up: Creating Organizational Wisdom Through an Ethic of Kaitiakitanga",
  lead="マオリの「カイティアキタンガ（守り手であること）」から、組織の知恵を考える。",
  s="ニュージーランドの先住民マオリには、人や土地、自然、そして将来の世代を守り世話する責任を表す「カイティアキタンガ」という考え方がある。著者らは、この倫理を手がかりに、組織が目先の利益を超えて、関係と時間の広がりの中で賢明に振る舞うための「組織の知恵」を論じる。組織の判断を、人間どうしの関係だけでなく、環境や先祖・子孫とのつながりの中に位置づける視点が示される。のちに同じ著者らが提唱する、ポリネシアの航海術に学ぶ「ウェイファインディング・リーダーシップ」へとつながる研究であり、先住民の知恵をリーダーシップに結びつける議論の入口になる。要旨は未入手で、書誌と二次的な紹介に基づく。"),
 dict(au="Chellie Spiller, Rachel Wolfgramm, Ella Henry, Robert Pouwhare", year=2020, src="Human Relations 73(4)", cites="113", grp="先住民の知恵", oa=False, basis="要旨",
  url="https://doi.org/10.1177/0018726719893753",
  title="Paradigm warriors: Advancing a radical ecosystems view of collective leadership from an Indigenous Māori perspective",
  lead="世代と生き物を超えて広がる、マオリの「生態系としての集合的リーダーシップ」。",
  s="集合的リーダーシップは新しい考え方として紹介されることが多いが、多くの先住民の共同体にとっては何千年も続いてきた生き方である、と著者らは指摘する。主流のモデルが「いまここ」で人々が何をし、考え、感じるかに注目するのに対し、マオリの見方は、過去と未来の世代や、生き物でないものまでを含む関係の広がりの中にリーダーシップを置く。著者らは、時間と空間を越えて集合的な知性を引き出すマオリの伝統的な学びの場「ワーナンガ」を研究方法として用い、3つの歴史的な場面を分析する。知の規範を働かせ、愛着の絆を育て、緊張を扱うことで保たれる「生態系」としてのリーダーシップを描く。"),
 dict(au="Linda Sue Warner, Keith Grint", year=2006, src="Leadership 2(2)", cites="107", grp="先住民の知恵", oa=False, basis="要旨",
  url="https://doi.org/10.1177/1742715006062936",
  title="American Indian Ways of Leading and Knowing",
  lead="アメリカ先住民のリーダーシップを、「導けない」のではなく「別の導き方」として描く。",
  s="アメリカ先住民のリーダーシップは、非先住民の観察者から「導く力がない」と誤解されてきたが、実際には「別の導き方」だった、と著者らは論じる。西洋のモデルは、本人たちの主張とは裏腹に地位に根ざし、個人を単位にしたものが多い。これに対し先住民のモデルは、人を説得する技法を重んじ、状況に応じた異なる形のリーダーシップが、個人の名声や報酬ではなく共同体に奉仕することを重視する。著者らは先住民の教育におけるリーダーシップを例に、書き言葉と話し言葉の使い分けを含む説得の方法に注目したモデルを示す。先住民の知恵とリーダーシップを結ぶ基本文献の一つである。"),
]
B_RES = [
 ("Shields（2004）", "Dialogic Leadership for Social Justice: Overcoming Pathologies of Silence", "Educational Administration Quarterly・被引用600（教育経営）"),
 ("Haar, Roche &amp; Brougham（2019）", "Indigenous Insights into Ethical Leadership: A Study of Māori Leaders", "Journal of Business Ethics・被引用83"),
 ("Verbos &amp; Humphries（2014）", "A Native American Relational Ethic", "Journal of Business Ethics・被引用83"),
 ("Julien, Wright &amp; Zinni（2010）", "Stories from the circle: Leadership lessons learned from aboriginal leaders", "The Leadership Quarterly・被引用60"),
]
B_BOOKS = ["Spiller, Barclay-Kerr &amp; Panoho『Wayfinding Leadership』（2015）", "Finney『Sailing in the Wake of the Ancestors: Reviving Polynesian Voyaging』（2004）",
           "Finney『Voyage of Rediscovery: A Cultural Odyssey through Polynesia』（1994）", "Dillon 編『Walking the Clouds: An Anthology of Indigenous Science Fiction』（2012）",
           "Bohm『On Dialogue』（1996）", "Isaacs『Dialogue and the Art of Thinking Together』（1999）"]


def card(p, n, pre):
    n2 = f"{n:02d}"
    tag = f' <span class="lit-tag">{p["grp"]}</span>' if p.get("grp") else (' <span class="lit-tag">人類学</span>' if p.get("anth") else "")
    st = '<span class="lit-st open">全文</span>' if p["oa"] else '<span class="lit-st paywall">購読</span>'
    stw, stn = ("全文", "無料で全文を読める") if p["oa"] else ("購読", "所属機関の契約か購入で読む")
    return f'''<section class="section" id="{pre}{n}">
  <div class="sec-head">
    <div class="eyebrow"><span class="n">{n2}</span>{html.escape(p['src'])} · {p['year']}{tag}</div>
    <h2>{html.escape(p['title'])}</h2>
    <p class="lead">{p['lead']}</p>
  </div>
  <div class="lit-meta people">
    <div><b>{html.escape(p['au'])}</b>著者</div>
    <div><b>{html.escape(p['src'])}</b>誌名<br><small>{p['year']}</small></div>
    <div><b class="mono">{p['cites']}</b>被引用<br><small>OpenAlex・{DATE}</small></div>
    <div><b>{stw}</b>本文の公開<br><small>{stn}</small></div>
  </div>
  <div class="lit-sumhead"><div class="subhead">概要</div><span class="lit-basis">根拠: {p['basis']}</span></div>
  <p class="lit-summary" data-id="{pre}{n}">{p['s']}</p>
  <p class="lit-link">{st}<a href="{p['url']}">{p['url']}</a></p>
</section>
'''


def toc_name(p):
    first = p["au"].split(",")[0].split("（")[0].strip()
    last = first.split(" ")[-1] if not re.search(r"[ぁ-んァ-ン一-龥]", first) else first
    more = " ほか" if "," in p["au"] else ""
    return f"{last}{more} {p['year']}"


def panel(pid, label, pre, papers, intro_h, intro_p, facts, method, res, books, limits):
    toc = "\n".join(f'      <a class="toc-item" href="#{pre}{i}"><span class="n">{i:02d}</span><span class="t">{html.escape(toc_name(p))}<small>{html.escape(p["title"][:58])}</small></span></a>'
                    for i, p in enumerate(papers, 1))
    cards = "".join(card(p, i, pre) for i, p in enumerate(papers, 1))
    rr = "\n".join(f'        <li>{a}『{t}』<small style="display:block;color:var(--es-ink-mute)">{s}</small></li>' for a, t, s in res)
    bb = "\n".join(f'        <li class="warn">{b}</li>' for b in books)
    fx = "\n".join(f'    <div class="fact"><div class="fact-label">{a}</div><div class="fact-num ink">{b}</div><div class="fact-desc">{c}</div></div>' for a, b, c in facts)
    return f'''<div class="lit-panel" id="{pid}" role="tabpanel" aria-labelledby="tabbtn-{pid}">
<main class="page">
<section class="section" id="{pre}intro">
  <div class="sec-head">
    <div class="eyebrow"><span class="n">00</span>{label}</div>
    <h2>{intro_h}</h2>
    <p class="lead">{intro_p}</p>
  </div>
  <div class="facts">
{fx}
  </div>
  <div class="note ink">{method}</div>
</section>
<section class="section" id="{pre}toc">
  <div class="sec-head"><div class="eyebrow"><span class="n">00</span>Contents</div><h2>目次</h2></div>
  <div class="toc">
    <div class="toc-col a">
      <div class="toc-head"><div class="letter">A</div><div class="lab"><small>Part A</small>主要論文10本</div></div>
{toc}
    </div>
    <div class="toc-col b">
      <div class="toc-head"><div class="letter">B</div><div class="lab"><small>Part B</small>付記</div></div>
      <a class="toc-item" href="#{pre}b1"><span class="n">B-1</span><span class="t">補欠と書籍<small>補欠{len(res)}本・書籍{len(books)}冊</small></span></a>
      <a class="toc-item" href="#{pre}limits"><span class="n">B-2</span><span class="t">この一覧の限界<small>検索範囲・概要の根拠・時点</small></span></a>
    </div>
  </div>
</section>
{cards}<section class="section" id="{pre}b1">
  <div class="sec-head"><div class="eyebrow"><span class="n">B-1</span>Reserve papers · Books</div><h2>補欠と書籍</h2>
    <p class="lead">10本に入れなかった補欠と、検索の対象外だった書籍。書籍は被引用数の比較に含めていない。</p></div>
  <div class="two">
    <div><div class="subhead">補欠（{len(res)}本）</div><ul class="pts">
{rr}
    </ul></div>
    <div><div class="subhead">書籍（{len(books)}冊）</div><ul class="pts">
{bb}
    </ul></div>
  </div>
</section>
<section class="section" id="{pre}limits">
  <div class="sec-head"><div class="eyebrow"><span class="n">B-2</span>Limits of this list</div><h2>この一覧の限界</h2></div>
  <div class="note ink">{limits}</div>
</section>
</main>
</div>
'''


def main():
    t = TEMPLATE.read_text(encoding="utf-8")
    head = t[t.index("<head>"):t.index("</head>") + len("</head>")]
    title = "未来の人類学 ― 読むべき主要論文"
    desc = "未来の人類学をめぐる主要論文10本と、先住民未来学・対話・先住民の知恵からリーダーシップを深める論文10本の文献一覧。著者・年・誌名・被引用数・300字程度の概要と、本文に無料で到達できるかを1枚にまとめた。"
    head = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", head)
    head = re.sub(r'(<meta name="description" content=")[^"]*', r"\g<1>" + desc, head)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*', r"\g<1>" + title, head)
    head = re.sub(r'(<meta property="og:description" content=")[^"]*', r"\g<1>" + desc, head)
    script = t[t.rindex("<script>"):t.rindex("</script>") + len("</script>")].replace("'tab-urban'", "'tab-future'")
    na = sum(p["oa"] for p in A); nb = sum(p["oa"] for p in B)
    pa = panel("tab-future", "Anthropology of the Future", "a", A,
        "未来の人類学を考えるために、まず読む10本",
        "人々は未来をどのように思い描き、待ち、備え、あるいは諦めてきたのか。未来を人類学の対象にする研究のうち、まず読んでおきたい10本を被引用数の多い順に並べた。時間の人類学、希望と予期、「善」の人類学という3つの流れにまたがる。",
        [("論文", '10<span class="unit">本</span>', "被引用数の多い順。補欠5本・書籍5冊を末尾に添える"),
         ("人類学", '10<span class="unit">本</span>', "すべて人類学の論文（02 は科学技術社会論と重なる）"),
         ("無料で全文を確認", f'{na}<span class="unit">本</span>', "02・06・07・08 番。残りは購読が必要"),
         ("被引用の範囲", '158<span class="unit">〜</span>1,227', f"OpenAlex・{DATE} 時点の値。以後は動く")],
        "選び方: OpenAlex で「anthropology of the future」「anticipation」「hope」「anthropology of time」「imagined futures」などの語を題名から検索し、被引用数の多い論文から未来の人類学に直接関わるものを選んだ。人類学以外の分野の論文（地理学・社会学）は補欠に回した。凡例: <b>全文</b>＝無料で全文を確認／<b>購読</b>＝購読が必要／<b>根拠: 要旨</b>＝著者の要旨に基づく／<b>根拠: 紹介</b>＝要旨が入手できず書誌と二次的な紹介に基づく（精度が他より低い）。",
        A_RES, A_BOOKS,
        "検索は英語の題名に限っており、日本語文献は含めていない。この分野の基本文献には書籍が多く（Fabian、宮崎、Appadurai、Bryant &amp; Knight）、論文の被引用数だけでは重要度を測れない。概要の根拠が「紹介」の項目（02・07）は要旨が入手できず、書誌と二次的な紹介に基づく。")
    pb = panel("tab-leadership", "Leadership · Second wave", "b", B,
        "先住民未来学・対話・先住民の知恵から、リーダーシップを深める10本",
        "第二陣として、リーダーシップの観点を深めるための論文を集めた。先住民未来学、ホクレア（ハワイの伝統航海カヌー）とリーダーシップ、対話とリーダーシップ、先住民の知恵とリーダーシップの4つの観点から、被引用数の多い順に10本を並べた。各論文の見出しに観点の印を付した。",
        [("論文", '10<span class="unit">本</span>', "被引用数の多い順。補欠4本・書籍6冊を末尾に添える"),
         ("観点の内訳", '3<span class="unit">群</span>', "対話4本・先住民の知恵4本・先住民未来学2本"),
         ("ホクレアと航海", '0<span class="unit">本</span>', "該当する論文は被引用が少なく、書籍3冊を挙げた（B-1）"),
         ("被引用の範囲", '107<span class="unit">〜</span>1,963', f"OpenAlex・{DATE} 時点の値。以後は動く")],
        "選び方: OpenAlex で「Indigenous futurism」「Indigenous futures」「relational leadership」「dialogue organizational learning」「Indigenous leadership」「Two-Eyed Seeing」「wayfinding leadership」「Polynesian voyaging」などの語を題名から検索し、被引用数の多い論文から観点に直接関わるものを選んだ。ホクレアとリーダーシップを直接扱う論文は、検索の範囲では被引用数が一桁以下にとどまったため10本には入れず、航海の復興を描いた書籍と、ポリネシアの航海術からリーダーシップを論じた書籍『Wayfinding Leadership』を挙げた。凡例は前のタブと同じ。",
        B_RES, B_BOOKS,
        "検索は英語の題名に限っており、日本語文献は含めていない。ホクレアとリーダーシップについては、論文より書籍・講演・団体の記録に知見が多く、この一覧では十分に拾えていない。対話の論文には経営学・組織論のものが多く、人類学の論文は含まれていない。概要の根拠が「紹介」の項目（01・02・03・04・07・08）は要旨が入手できず、書誌と二次的な紹介に基づくため、精度が他より低い。")
    nav = '''<nav class="lit-tabs" aria-label="文献一覧の切り替え"><div class="lit-tabs-inner" role="tablist">
  <a class="lit-tab" role="tab" id="tabbtn-tab-future" href="#tab-future" aria-controls="tab-future"><span class="n">01</span>未来の人類学</a>
  <a class="lit-tab" role="tab" id="tabbtn-tab-leadership" href="#tab-leadership" aria-controls="tab-leadership"><span class="n">02</span>第二陣: 先住民の知恵 × 対話 × リーダーシップ</a>
</div></nav>
'''
    body = f'''<body>
<a class="skip-link" href="#tab-future">本文へスキップ</a>
<header class="cover lit-nophoto" role="banner">
  <div class="cover-panel">
    <div class="cover-head"><img class="brand-logo" src="assets/esse-sense-logo-white.png" alt="esse-sense"><span>Reading list ｜ Public</span></div>
    <div class="cover-main">
      <div class="cover-eyebrow">Reading List · 2026.10</div>
      <h1 class="cover-title doc-title">未来の<br>人類学</h1>
      <div class="cover-sub">読むべき主要論文 ― 未来の人類学と、先住民の知恵・対話から深めるリーダーシップ</div>
      <div class="cover-rule"></div>
      <div class="cover-meta">2026.10.16 ／ esse-sense.inc<br>タブ1: 未来の人類学 論文10本 ／ タブ2: リーダーシップ（第二陣）論文10本 ／ 被引用数は OpenAlex {DATE} 時点</div>
    </div>
    <div class="cover-foot"><span>esse-sense.inc</span><span>Public</span></div>
  </div>
</header>
<div class="topbar"><div class="topbar-inner"><img class="brand-logo" src="assets/esse-sense-logo.png" alt="esse-sense"><div class="doc">未来の人類学 ― 読むべき主要論文</div><div class="num">2026.10</div></div></div>
{nav}{pa}{pb}
<footer class="foot"><div>esse-sense.inc</div><div class="c">未来の人類学 ― 読むべき主要論文 ・ 2026.10</div><div class="mono">v1.0</div></footer>
{script}
</body>
</html>
'''
    comment = "<!--\n  型: urban-memory-reading-list/index.html の head（esse-sense 基礎レポートデザイン /esrep の写し＋文献一覧の部品＋タブ）をそのまま使い、本文だけを差し替えた。\n  生成: tools/build.py（再実行で上書き）。書誌と被引用数は OpenAlex 2026-10-16。\n-->\n"
    OUT.write_text("<!DOCTYPE html>\n" + comment + '<html lang="ja">\n' + head + "\n" + body, encoding="utf-8")


if __name__ == "__main__":
    main()
