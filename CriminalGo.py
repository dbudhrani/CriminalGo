import csv
import os

from mrjob.runner import MRJobRunner

from models import Pokemon
from models import CrimeRecord
from models import CrimeCluster
from logic import BuildCrimeAreas
from logic import PointInPolygon
from logic import PokemonPredictor
import numpy as np

def main():

	pokepredictor = PokemonPredictor()
	pokepredictor.predictPokemonAppearances()

'''
	mr_job = BuildCrimeAreas(args=['datasets/Crimes_-_2001_to_present.csv'])
	with mr_job.make_runner() as runner:
		runner.run()
		for line in runner.stream_output():
			key, value = mr_job.parse_output_line(line)
			print "key = " + str(key) + "; value = " + str(value)
'''


'''
	pip = PointInPolygon()
	commAreas = open(os.path.join(os.path.dirname(__file__), 'datasets/CommAreas.csv'))
	commReader = csv.reader(commAreas, delimiter=',')
	for communities in commReader:
		a = np.matrix(communities[0])
	#a = np.matrix("-87.60914087617012 41.8446925034611; -87.60914874756925 41.84466159923116; -87.60916112040377 41.84458961274664; -87.60916766214955 41.84451717813025; -87.60916860599283 41.84445626154538; -87.60915012198514 41.844238717405155; -87.60907241248407 41.84419473968805; -87.60900627146938 41.84410647009398; -87.60896502171278 41.84404345835816; -87.6089156638973 41.843955294557524; -87.60889980118105 41.84387361730229; -87.6088670137098 41.84380438360743; -87.60885143423607 41.843697607767794; -87.60881089280211 41.84357184857331; -87.60877127221904 41.843364517960396; -87.60872156081648 41.84330772777204; -87.60867220388796 41.84321956386265; -87.60858152788133 41.843074662907995; -87.60847385681988 41.84294847996566; -87.60839135989272 41.84282245609141; -87.60826740294763 41.84265224417277; -87.60817672827486 41.842507342895516; -87.6080691301754 41.84237488500156; -87.60801956188496 41.84230554481001; -87.60802097918128 41.842180050547256; -87.60799814395999 41.841972825347234; -87.6079750257652 41.84179069954187; -87.6079766557274 41.84164638099073; -87.6079781439466 41.84151461158924; -87.60797949041941 41.84139539188711; -87.60794734336663 41.84126968535609; -87.60789016476008 41.841131270664874; -87.60784934324849 41.84103060995981; -87.60773349880778 41.84088554931062; -87.60765630432459 41.84076193873921; -87.60757583126387 41.84063822012952; -87.60752760501985 41.84056030853322; -87.60698398203101 41.84066738604876; -87.60667816424403 41.84056137339439; -87.60671361513975 41.84050343637542; -87.60699497653887 41.84060011061274; -87.60750090432069 41.84050284568744; -87.60746117925359 41.840459950756745; -87.60744220350448 41.840418505566596; -87.6074332704139 41.840393960429; -87.60743661712011 41.8403694923513; -87.60743928898263 41.840365282528; -87.60745016249727 41.840348150225395; -87.60741319769637 41.84026855836181; -87.60734791404366 41.84010499150254; -87.60721091961612 41.83965162879595; -87.6070952300635 41.839512037765324; -87.60700484632396 41.83945658074733; -87.60694131396686 41.83942818778112; -87.60690335603505 41.839409835870484; -87.60682817414478 41.83937313583088; -87.60676104001784 41.839338682334564; -87.60670126503234 41.83930262907422; -87.60666194500965 41.83927493743137; -87.6066204733688 41.83924284161879; -87.60658411310668 41.83921297354175; -87.60651223399354 41.83914391191648; -87.60649228112257 41.83912449706636; -87.6064679500338 41.839100822032144; -87.60645125092643 41.83908479909034; -87.60615627838726 41.8386350219308; -87.60614048964037 41.83863857018922; -87.60470984484891 41.83896006145735; -87.6042777301301 41.83958213977973; -87.60427494700046 41.83982732780842; -87.60418506321405 41.839828573656014; -87.60419546273982 41.8395543725384; -87.60466703486144 41.8388798709645; -87.60613498879054 41.838551276645155; -87.60613594089122 41.83852105161993; -87.60612905109754 41.83843916892108; -87.60611500647559 41.838298784591736; -87.60610096227762 41.838158400260085; -87.60607903536552 41.83802381183705; -87.60610453594293 41.83784275792806; -87.60609890364316 41.837649816061955; -87.60608545485236 41.83745682442305; -87.6060716752297 41.83729305926258; -87.6060191456668 41.83709982014393; -87.60597489580955 41.8368657142905; -87.6059147490214 41.836654890216735; -87.60588836936232 41.836573039093714; -87.60584678659262 41.836444016327604; -87.6057701475616 41.83630908098499; -87.60565502444084 41.83612129098373; -87.60551618881472 41.83595673281761; -87.60530826792214 41.83568067000142; -87.60509186988871 41.835463009406816; -87.60482102657403 41.83522162004449; -87.6046429823647 41.83506850431385; -87.60455786851077 41.83499197045582; -87.60454429253178 41.83481066940606; -87.60473439459709 41.83458974057311; -87.60503332162249 41.834422112593614; -87.60499603130611 41.83426404342431; -87.6049439049819 41.834035732677144; -87.60486846409401 41.833795582649294; -87.6047455982643 41.833601897005174; -87.60463015101621 41.833443331896135; -87.60455305424416 41.83334931248788; -87.60443687877189 41.83325504476559; -87.60435156855027 41.833196046978436; -87.60422717999832 41.83313680107197; -87.604071528477 41.833077356540784; -87.60391567814999 41.8330354472025; -87.603751680516 41.83302271422805; -87.60361099735053 41.83302182052834; -87.6034860782174 41.83300933571538; -87.6033536756205 41.832967574605604; -87.60322922201611 41.83291417276021; -87.6031284811347 41.832837539036326; -87.60301244158188 41.83273157962239; -87.60291229935893 41.832602338414226; -87.60279652682183 41.832472997704706; -87.60270433427128 41.83233211576045; -87.6027053978702 41.832238591982225; -87.60273083857304 41.83206338437815; -87.60276449414434 41.83185315512621; -87.60276542470062 41.831771321881014; -87.60273575744247 41.83163083762258; -87.6027295376769 41.831490502226586; -87.60271020372586 41.83136624767305; -87.60279792683366 41.83136620629781; -87.60295002258202 41.83133289248667; -87.60583494109139 41.831233948618184; -87.60604987531589 41.83123284431512; -87.60620267768667 41.831238202292134; -87.60670209232119 41.831232855293386; -87.60686720985719 41.83123287064628; -87.60721395666842 41.83123300502443; -87.60749035996226 41.83121712014999; -87.60828613363422 41.831209306309496; -87.60903306354382 41.83120196683823; -87.60939573918839 41.83119840140233; -87.61063335778184 41.83118622542001; -87.61100082837845 41.82977587133291; -87.61100977741125 41.82974683839717; -87.61102002074671 41.829716907992335; -87.61108240937088 41.829493834770474; -87.61127644642686 41.82879669397119; -87.61127692970703 41.82879495879123; -87.6112950704349 41.828729780155626; -87.61129609251094 41.828726103775665; -87.61133106843377 41.82860044278191; -87.61141795483671 41.828288269355035; -87.61141940967293 41.82828304161566; -87.6114830835377 41.82805426482759; -87.6115241788928 41.827906611521044; -87.61162668483021 41.82753626072759; -87.61168992269698 41.82730778374622; -87.61184008667637 41.826766350196024; -87.61188696986694 41.82659407474316; -87.61194857939992 41.826367685892954; -87.61205793721943 41.82597292374984; -87.6121279287 41.8257227421971; -87.61225564052701 41.82526241183631; -87.61237128465226 41.82484023073088; -87.61257695181631 41.82408938784097; -87.6126242723945 41.82389080517135; -87.61307586545516 41.82388477628119; -87.61436403577905 41.82386898820399; -87.61514774091994 41.82385938205802; -87.61547482917396 41.82385537231098; -87.61610922731991 41.823847592335895; -87.61673229763211 41.82383813937483; -87.6169968247497 41.823834107646256; -87.61725854541707 41.82383011791209; -87.61770996886861 41.823823235209524; -87.61794972729027 41.82382029561154; -87.61821435997896 41.82381705071321; -87.6185513181061 41.82381291801811; -87.61886174703943 41.823809109721985; -87.61917760591544 41.823805230613736; -87.61998816930563 41.823795271862544; -87.62039535937376 41.82379026692264; -87.62095332331079 41.823783406457096; -87.62160197732236 41.823775267423855; -87.62222982585945 41.82376738616025; -87.62234636528846 41.82376591682915; -87.62240779066713 41.82376514223724; -87.62314672393556 41.823755822672716; -87.62426776089141 41.82374167463069; -87.62432122057021 41.82374128261319; -87.62446432459515 41.82373962219041; -87.62482271021824 41.823735732859326; -87.62497215616358 41.82373411064784; -87.62531936393765 41.82372867716026; -87.62559794621336 41.82372485056514; -87.62574361150479 41.82372311459192; -87.62591974776295 41.8237210153253; -87.62608002879398 41.8237187363846; -87.62642224680934 41.82371376417948; -87.62661202559408 41.823711006309516; -87.62698708870555 41.82370809923335; -87.627224939577 41.82370489637566; -87.6275934143608 41.82369902444583; -87.6277344869874 41.82369677610998; -87.62806959945627 41.823690217183824; -87.62830656308215 41.823687582934824; -87.6286179305429 41.82368504218739; -87.62876532190091 41.82368383904767; -87.62896819970506 41.82368149243281; -87.62902443060024 41.82525934879928; -87.62903126473664 41.825453979390474; -87.62903952948209 41.82568941339695; -87.62904559797889 41.825885583478275; -87.62909202843329 41.82733017648514; -87.62907827723242 41.82742323234727; -87.62904767936446 41.82751006574274; -87.62898825423991 41.82758239700914; -87.62893520543312 41.82763876826659; -87.62892312908924 41.82767939169618; -87.62893235141564 41.82785560278971; -87.6289368271293 41.82802969885078; -87.62894162228869 41.828254950558154; -87.62894615001736 41.82848127088084; -87.62894944328568 41.82864605660577; -87.62895135774377 41.82874004934225; -87.6289534503892 41.82884279024684; -87.62895931484303 41.829074332576454; -87.62896232304567 41.829190320177425; -87.62896563326224 41.82931795245465; -87.62897263322138 41.82958984244916; -87.62898034189945 41.829890771117206; -87.62898715370824 41.83015640300289; -87.62899259211616 41.83036985795096; -87.62899941196915 41.83064139003593; -87.62900366241217 41.83083274633864; -87.6289956829872 41.83097495028413; -87.62914494786489 41.83097286354253; -87.62924490109565 41.83097146611805; -87.62938395426835 41.83097119601611; -87.62947678530243 41.83097101545541; -87.6295304775206 41.83097091087028; -87.62956105279402 41.83097085150512; -87.6295655112393 41.83105962866274; -87.62958360078488 41.831753009126004; -87.62961050449105 41.83277232556586; -87.62961560755063 41.832976462105876; -87.6296211040218 41.8332090700547; -87.62962751661625 41.83348045073996; -87.62964438185726 41.8341601020829; -87.62964450668944 41.83416451754617; -87.62965495204898 41.83453510198224; -87.62965689610574 41.83461359464075; -87.62965717449237 41.83462482862046; -87.629662398187 41.83481301369886; -87.62966276948393 41.83482638520598; -87.62968729954054 41.83581138352726; -87.62969845480355 41.83620399382232; -87.62972206128597 41.83703485168352; -87.62973867442305 41.837568130026575; -87.62976040511526 41.83826567253957; -87.62976266726227 41.83835303270967; -87.62978240744162 41.839099865525235; -87.62978731525807 41.8392855465754; -87.62979312535919 41.83950889677161; -87.6298008997375 41.839804295318864; -87.62981523196025 41.840338485341405; -87.62982944638786 41.84086397994831; -87.62984200585437 41.84132829835443; -87.62985750746304 41.841713961992546; -87.62986099277367 41.841835079620594; -87.62986309716192 41.841908213892495; -87.62986619607899 41.84201589324835; -87.6298755442388 41.842337157179344; -87.62988457174264 41.84278617351453; -87.62990488052863 41.843344480467785; -87.62991425093101 41.84376221425837; -87.62992853161467 41.844275669609196; -87.6299306071058 41.844346292949076; -87.62994472511093 41.84479973111627; -87.62996222539653 41.84541345470652; -87.62996524444752 41.84554483375245; -87.62996524439643 41.84554483841737; -87.62978701012575 41.84554552011293; -87.62946563464423 41.845553059096346; -87.62916818463978 41.845556606623276; -87.62872700195979 41.84556186722146; -87.6284606879554 41.84556618817687; -87.62812269391209 41.845570790433015; -87.62791754031569 41.845573583594046; -87.62765212479316 41.84557628907969; -87.62723696033015 41.84557971998496; -87.62696086826935 41.8455851066111; -87.62675994850636 41.84558902638596; -87.62637708858657 41.84559649432633; -87.62626462169902 41.84559832233756; -87.62619207700543 41.84559950113792; -87.62618268754152 41.845599653812606; -87.62614381812257 41.84560028551727; -87.6261320650495 41.84560047659863; -87.62610277230249 41.84560095265514; -87.62579736038123 41.84560626159301; -87.6255389038337 41.84561023997993; -87.62532610033784 41.84561360404043; -87.62479326358367 41.845622025744795; -87.62446484493238 41.84562674079504; -87.62417259010917 41.84563048939017; -87.62407957620545 41.84563171719844; -87.6236362047631 41.845638284468805; -87.62339191456321 41.845641902085696; -87.62213772958515 41.845660470963985; -87.62048133129089 41.845684964133085; -87.62033059867882 41.84568719208082; -87.61886420373013 41.84571019884057; -87.61783987811785 41.845726258792666; -87.61767140559559 41.84572320337666; -87.61729852316135 41.84566818215142; -87.61720985189288 41.845655097932685; -87.61692091129596 41.845644514377646; -87.61666117917208 41.84564437588204; -87.61661825063868 41.845643284729; -87.61659503182254 41.84564215190312; -87.61657183469312 41.845639043341876; -87.61655066437635 41.84563194080776; -87.61652626795411 41.845617875162006; -87.61650393113082 41.84559687939186; -87.61647763859752 41.845571879753464; -87.61645798625278 41.84555037932018; -87.61643788912791 41.845526049521126; -87.61625954806448 41.84523119079309; -87.61623779940655 41.845200236983864; -87.61621749507974 41.84517804637305; -87.61619627182667 41.84515917057376; -87.61616875932155 41.84514162762906; -87.61613940344323 41.84512805234193; -87.6161002121301 41.84511444307074; -87.61607353455582 41.84510423276182; -87.6160352009613 41.84509597985459; -87.61600840419449 41.845093123124634; -87.61596180511143 41.84509217345769; -87.61511263998153 41.84510687214145; -87.61499270628724 41.84510993387022; -87.61500079131055 41.84516621703666; -87.61400068995992 41.84516647536757; -87.61350109943116 41.84516643236027; -87.61240099156913 41.84516639324705; -87.61192963328182 41.84522518132672; -87.6115808890711 41.84526623543961; -87.61141060497297 41.845266549713436; -87.61112256410892 41.8452664397457; -87.61091654921505 41.84526644902026; -87.60940614539751 41.845266504793145; -87.60940949181392 41.8452177340755; -87.60937658091395 41.84515338344386; -87.60914087617012 41.8446925034611")
		inside = pip.checkInside("41.740918989", "-87.631967753", a)	
		if inside:
			print "good, " + communities[6] + " " + str(communities[5])
		inside = pip.checkInside("41.9741665", "-87.9095101", a)	
		if inside:
			print "good, " + communities[6] + " " + str(communities[5])
		inside = pip.checkInside("41.9872003", "-87.678661", a)	
		if inside:
			print "good, " + communities[6] + " " + str(communities[5])

	#	else:
	#		print "bad:("
'''


def loadPokemonTypes():
	with open("datasets/pokemon.csv") as input:
		reader = csv.reader(input, delimiter=';')
		for row in reader:
			pokemon = Pokemon(row[0], row[1], row[2])
			print "ID = " + str(pokemon.id) + "; Name = " + pokemon.name + "; Rareness = " + str(pokemon.rareness)

def loadCrimes():
	with open("datasets/Crimes_-_2001_to_present.csv") as input:
		reader = csv.reader(input, delimiter=',')
		i = 0
		next(reader)	# we skip the header row
		for row in reader:
			crime = CrimeRecord(row[0], row[2], row[4], row[7], row[9], row[11], row[17], row[19], row[20])
			if (i < 100):
				print "ID = " + str(crime.id) + "; Date = " + crime.date + "; IUCR = " + str(crime.IUCR) + "; Location description = " + crime.locationDescription + "; Domestic = " + crime.domestic + "; District = " + crime.district + "; Year = " + str(crime.year) + "; Latitude = " + crime.latitude + "; Longitude = " + str(crime.longitude)
			i = i + 1

if __name__ == "__main__":
	main()