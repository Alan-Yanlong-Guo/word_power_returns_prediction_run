def word_filter(word):
    first_letter = word[0]
    if first_letter == 'a':
        word = word_filter_a(word)
    elif first_letter == ('b' or 'c'):
        word = word_filter_bc(word)
    elif first_letter == ('d' or 'e'):
        word = word_filter_de(word)
    elif first_letter == ('f' or 'g' or 'h'):
        word = word_filter_fgh(word)
    elif first_letter == 'i':
        word = word_filter_i(word)
    elif first_letter == ('j' or 'k' or 'l' or 'm'):
        word = word_filter_jklm(word)
    elif first_letter == ('n' or 'o'):
        word = word_filter_no(word)
    elif first_letter == ('p' or 'q'):
        word = word_filter_pq(word)
    elif first_letter == ('r' or 's'):
        word = word_filter_rs(word)
    elif first_letter == 't':
        word = word_filter_t(word)
    elif first_letter == 'u':
        word = word_filter_u(word)
    elif first_letter == ('v' or 'w'):
        word = word_filter_vw(word)
    return word


def word_filter_a(word):
    # 34 word-roots
    if 'abandon' in word:
        return 'abandon'
    elif 'abdicat' in word:
        return 'abdicate'
    elif 'aberra' in word:
        return 'aberrant'
    elif 'abetting' in word:
        return 'abetting'
    elif 'abnormal' in word:
        return 'abnormal'
    elif 'abolish' in word:
        return 'abolish'
    elif 'abrogat' in word:
        return 'abrogate'
    elif 'abrupt' in word:
        return 'abrupt'
    elif 'absen' in word:
        return 'absence'
    elif 'abus' in word:
        return 'abuse'
    elif 'accid' in word:
        return 'accident'
    elif 'accus' in word:
        return 'accuse'
    elif 'acquie' in word:
        return 'acquiesce'
    elif 'adulterat' in word:
        return 'adulterate'
    elif 'advers' in word:
        return 'adverse'
    elif 'aftermath' in word:
        return 'aftermath'
    elif 'against' in word:
        return 'against'
    elif 'aggravat' in word:
        return 'aggravate'
    elif 'alert' in word:
        return 'alert'
    elif 'alienat' in word:
        return 'alienate'
    elif 'alleg' in word:
        return 'allege'
    elif 'annoy' in word:
        return 'annoy'
    elif 'annul' in word:
        return 'annul'
    elif 'anomal' in word:
        return 'anomaly'
    elif 'anticompetitive' in word:
        return 'anticompetitive'
    elif 'antitrust' in word:
        return 'antitrust'
    elif 'argu' in word:
        return 'argue'
    elif 'arrear' in word:
        return 'arrearage'
    elif 'arrest' in word:
        return 'arrest'
    elif 'artificially' in word:
        return 'artificially'
    elif 'assault' in word:
        return 'assault'
    elif 'assertion' in word:
        return 'assertion'
    elif 'attrition' in word:
        return 'attrition'
    elif 'aversely' in word:
        return 'aversely'
    elif 'able' in word:
        return 'able'
    elif 'abundan' in word:
        return 'abundant'
    elif 'acclaimed' in word:
        return 'acclaimed'
    elif 'accomplish' in word:
        return 'accomplish'
    elif 'achiev' in word:
        return 'achieve'
    elif 'adequately' in word:
        return 'adequately'
    elif 'advanc' in word:
        return 'advance'
    elif 'advantag' in word:
        return 'advantage'
    elif 'alliance' in word:
        return 'alliance'
    elif 'assur' in word:
        return 'assure'
    elif 'attain' in word:
        return 'attain'
    elif 'attractive' in word:
        return 'attractive'


def word_filter_bc(word):
    if 'backdating' in word:
        return 'backdating'
    elif 'bad' in word:
        return 'bad'
    elif 'bail' in word:
        return 'bail'
    elif 'balk' in word:
        return 'balk'
    elif 'bankrupt' in word:
        return 'bankrupt'
    elif 'bans' in word:
        return 'bans'
    elif 'barr' in word:
        return 'barred'
    elif 'bottleneck' in word:
        return 'bottleneck'
    elif 'boycott' in word:
        return 'boycott'
    elif 'breach' in word:
        return 'breach'
    elif ('break' or 'broken') in word:
        return 'break'
    elif 'bribe' in word:
        return 'bribe'
    elif 'birdge' in word:
        return 'bridge'
    elif 'burden' in word:
        return 'burden'
    elif 'beautiful' in word:
        return 'beautiful'
    elif ('benefit' or 'benefic') in word:
        return 'benefit'
    elif 'best' in word:
        return 'best'
    elif 'better' in word:
        return 'better'
    elif 'bolster' in word:
        return 'bolster'
    elif 'boom' in word:
        return 'boom'
    elif 'boost' in word:
        return 'boost'
    elif 'breakthrough' in word:
        return 'breakthrough'
    elif 'brilliant' in word:
        return 'brilliant'
    elif 'calamit' in word:
        return 'calamity'
    elif 'cancel' in word:
        return 'cancel'
    elif 'careless' in word:
        return 'careless'
    elif 'catastroph' in word:
        return 'catastrophe'
    elif 'caution' in word:
        return 'caution'
    elif 'cease' in word:
        return 'cease'
    elif 'censur' in word:
        return 'censure'
    elif 'challenge' in word:
        return 'challenge'
    elif 'chargeoffs' in word:
        return 'chargeoffs'
    elif 'circumvent' in word:
        return 'circumvent'
    elif 'claim' in word:
        return 'claim'
    elif 'clawback' in word:
        return 'clawback'
    elif 'clos' in word:
        return 'close'
    elif 'coerc' in word:
        return 'coerce'
    elif 'collaps' in word:
        return 'collapse'
    elif ('collision' or 'collide') in word:
        return 'collision'
    elif 'collud' in word:
        return 'collude'
    elif 'complain' in word:
        return 'complain'
    elif 'complicat' in word:
        return 'complicate'
    elif 'compuls' in word:
        return 'compulsion'
    elif 'conceal' in word:
        return 'conceal'
    elif 'conced' in word:
        return 'concede'
    elif 'concern' in word:
        return 'concern'
    elif 'conciliat' in word:
        return 'conciliate'
    elif 'condemn' in word:
        return 'condemn'
    elif 'condon' in word:
        return 'condone'
    elif 'confess' in word:
        return 'confess'
    elif 'cofin' in word:
        return 'confine'
    elif 'confisgat' in word:
        return 'confisgate'
    elif 'conflict' in word:
        return 'conflict'
    elif 'confront' in word:
        return 'confront'
    elif 'confus' in word:
        return 'confuse'
    elif 'conspir' in word:
        return 'conspire'
    elif 'comtempt' in word:
        return 'comtempt'
    elif 'contend' in word:
        return 'contend'
    elif 'content' in word:
        return 'contention'
    elif 'contest' in word:
        return 'contest'
    elif 'contradict' in word:
        return 'contradict'
    elif 'contrary' in word:
        return 'contrary'
    elif 'controvers' in word:
        return 'controvers'
    elif 'convict' in word:
        return 'convict'
    elif 'correct' in word:
        return 'correct'
    elif 'corrupt' in word:
        return 'corrupt'
    elif 'costly' in word:
        return 'costly'
    elif 'conterclaim' in word:
        return 'conterclaim'
    elif 'counterfeit' in word:
        return 'counterfeit'
    elif 'countermeasure' in word:
        return 'countermeasure'
    elif 'crim' in word:
        return 'crime'
    elif ('crisis' or 'crises') in word:
        return 'crisis'
    elif 'critic' in word:
        return 'criticize'
    elif 'crucial' in word:
        return 'crucial'
    elif 'culpab' in word:
        return 'culpable'
    elif 'cumbersome' in word:
        return 'cumbersome'
    elif 'curtail' in word:
        return 'curtail'
    elif 'cut' in word:
        return 'cut'
    elif 'cyberattack' in word:
        return 'cyberattack'
    elif 'cyberbullying' in word:
        return 'cyberbullying'
    elif 'cybercrim' in word:
        return 'cybercrime'
    elif 'charitable' in word:
        return 'charitable'
    elif 'collaborat' in word:
        return 'collaborate'
    elif 'compliment' in word:
        return 'compliment'
    elif 'conclusive' in word:
        return 'conclusive'
    elif 'conducive' in word:
        return 'conducive'
    elif 'confident' in word:
        return 'confident'
    elif 'constructive' in word:
        return 'constructive'
    elif 'courteous' in word:
        return 'courteous'
    elif 'creativ' in word:
        return 'creative'


def word_filter_de(word):
    if 'damag' in word:
        return 'damage'
    elif 'dampen' in word:
        return 'dampen'
    elif 'danger' in word:
        return 'danger'
    elif 'deadlock' in word:
        return 'deadlock'
    elif 'deadweight' in word:
        return 'deadweight'
    elif 'debar' in word:
        return 'debar'
    elif 'decrease' in word:
        return 'decrease'
    elif 'deceit' in word:
        return 'deceit'
    elif 'deceiv' in word:
        return 'deceive'
    elif 'decep' in word:
        return 'deception'
    elif 'declin' in word:
        return 'decline'
    elif 'defac' in word:
        return 'deface'
    elif 'defam' in word:
        return 'defame'
    elif 'default' in word:
        return 'default'
    elif 'defeat' in word:
        return 'defeat'
    elif 'defect' in word:
        return 'defect'
    elif 'defend' in word:
        return 'defen'
    elif 'defer' in word:
        return 'defer'
    elif 'deficien' in word:
        return 'deficient'
    elif 'deficit' in word:
        return 'deficit'
    elif 'defraud' in word:
        return 'defraud'
    elif 'defunct' in word:
        return 'defunct'
    elif 'degrad' in word:
        return 'degrade'
    elif 'delay' in word:
        return 'delay'
    elif 'deleterious' in word:
        return 'deleterious'
    elif 'deliberate' in word:
        return 'deliberate'
    elif 'delinquen' in word:
        return 'delinquent'
    elif 'delist' in word:
        return 'delist'
    elif 'demis' in word:
        return 'demise'
    elif 'demoli' in word:
        return 'demolish'
    elif 'demot' in word:
        return 'demote'
    elif ('denial' or 'denie' or 'deny') in word:
        return 'deny'
    elif 'denigrat' in word:
        return 'denigrate'
    elif 'deplet' in word:
        return 'deplete'
    elif 'depreciat' in word:
        return 'depreciate'
    elif 'depress' in word:
        return 'depress'
    elif 'depriv' in word:
        return 'deprive'
    elif 'derelict' in word:
        return 'derelict'
    elif 'derogatory' in word:
        return 'derogatory'
    elif 'destabiliz' in word:
        return 'destabilize'
    elif ('destroy' or 'destruct') in word:
        return 'destroy'
    elif ('detain' or 'detent') in word:
        return 'detain'
    elif 'deteriorat' in word:
        return 'deteriorate'
    elif 'deter' in word:
        return 'deter'
    elif 'detract' in word:
        return 'detract'
    elif 'detriment' in word:
        return 'detriment'
    elif 'devalu' in word:
        return 'devalue'
    elif 'devastat' in word:
        return 'devastate'
    elif 'deviat' in word:
        return 'deviate'
    elif 'devolv' in word:
        return 'devolve'
    elif 'difficult' in word:
        return 'difficult'
    elif ('diminish' or 'deminution') in word:
        return 'diminish'
    elif 'disadvantage' in word:
        return 'disadvantage'
    elif 'disaffiliation' in word:
        return 'disaffiliation'
    elif 'disagree' in word:
        return 'disagree'
    elif 'disallow' in word:
        return 'disallow'
    elif 'disappear' in word:
        return 'disappear'
    elif 'disappoint' in word:
        return 'disappoint'
    elif 'disapprov' in word:
        return 'disapprove'
    elif 'disassociat' in word:
        return 'disassociate'
    elif 'disast' in word:
        return 'disaster'
    elif 'disavow' in word:
        return 'disavow'
    elif 'disciplin' in word:
        return 'discipline'
    elif 'disclaim' in word:
        return 'disclaim'
    elif 'disclos' in word:
        return 'disclose'
    elif 'discontinu' in word:
        return 'discontinue'
    elif 'discourag' in word:
        return 'discourage'
    elif 'discredit' in word:
        return 'discredit'
    elif 'discrepanc' in word:
        return 'discrepancy'
    elif 'disfavor' in word:
        return 'disfavor'
    elif 'disgorg' in word:
        return 'disgorge'
    elif 'disgrac' in word:
        return 'disgrace'
    elif 'dishonest' in word:
        return 'dishonest'
    elif 'dishonor' in word:
        return 'dishonor'
    elif 'disincentive' in word:
        return 'disincentive'
    elif 'disinterest' in word:
        return 'disinterest'
    elif 'disloyal' in word:
        return 'disloyal'
    elif 'dismal' in word:
        return 'dismal'
    elif 'dismiss' in word:
        return 'dismiss'
    elif 'disorder' in word:
        return 'disorder'
    elif 'disparag' in word:
        return 'disparage'
    elif 'disparit' in word:
        return 'disparity'
    elif 'displac' in word:
        return 'displace'
    elif 'dispos' in word:
        return 'dispose'
    elif 'disproportion' in word:
        return 'disproportion'
    elif 'disput' in word:
        return 'dispute'
    elif 'disqualif' in word:
        return 'disqualify'
    elif 'disregard' in word:
        return 'disregard'
    elif 'disreput' in word:
        return 'disrepute'
    elif 'disrupt' in word:
        return 'disrupt'
    elif 'dissatisf' in word:
        return 'dissatisfy'
    elif 'dissent' in word:
        return 'dissent'
    elif 'dissident' in word:
        return 'dissident'
    elif 'dissolution' in word:
        return 'dissolution'
    elif 'distort' in word:
        return 'distort'
    elif 'distract' in word:
        return 'distract'
    elif 'distress' in word:
        return 'distress'
    elif 'disturb' in word:
        return 'disturb'
    elif 'diver' in word:
        return 'divert'
    elif 'divest' in word:
        return 'divest'
    elif 'divorce' in word:
        return 'divorce'
    elif 'divulge' in word:
        return 'divulge'
    elif 'doubt' in word:
        return 'doubt'
    elif 'downgrad' in word:
        return 'downgrade'
    elif 'downsiz' in word:
        return 'downsize'
    elif 'downtime' in word:
        return 'downtime'
    elif 'downturn' in word:
        return 'downturn'
    elif 'downward' in word:
        return 'downward'
    elif 'drag' in word:
        return 'drag'
    elif 'drastic' in word:
        return 'drastic'
    elif 'drawback' in word:
        return 'drawback'
    elif 'dropped' in word:
        return 'dropped'
    elif 'drought' in word:
        return 'drought'
    elif 'duress' in word:
        return 'duress'
    elif 'dysfunction' in word:
        return 'dysfunction'
    elif 'delight' in word:
        return 'delight'
    elif 'dependable' in word:
        return 'dependable'
    elif 'desir' in word:
        return 'desire'
    elif 'despite' in word:
        return 'despite'
    elif 'destined' in word:
        return 'destined'
    elif 'diligent' in word:
        return 'diligent'
    elif 'distinct' in word:
        return 'distinctive'
    elif 'dream' in word:
        return 'dream'
    elif 'easing' in word:
        return 'easing'
    elif 'egregious' in word:
        return 'egregious'
    elif 'embargo' in word:
        return 'embargo'
    elif 'embarrass' in word:
        return 'embarrass'
    elif 'embezzl' in word:
        return 'embezzle'
    elif 'encroach' in word:
        return 'encroach'
    elif 'encumber' in word:
        return 'encumber'
    elif 'endanger' in word:
        return 'endanger'
    elif 'enjoin' in word:
        return 'enjoin'
    elif ('erod' or 'erosion') in word:
        return 'erode'
    elif 'err' in word:
        return 'error'
    elif 'escalat' in word:
        return 'escalate'
    elif ('evad' or 'evas') in word:
        return 'evade'
    elif 'evict' in word:
        return 'evict'
    elif 'exacerbat' in word:
        return 'exacerbate'
    elif 'exaggerat' in word:
        return 'exaggerate'
    elif 'excessive' in word:
        return 'excessive'
    elif 'exculpat' in word:
        return 'exculpate'
    elif 'exonerat' in word:
        return 'exonerate'
    elif 'exploit' in word:
        return 'exploit'
    elif 'expos' in word:
        return 'expose'
    elif 'expropriat' in word:
        return 'expropriate'
    elif 'expulsion' in word:
        return 'expulsion'
    elif 'extenuating' in word:
        return 'extenuating'
    elif ('easi' or 'easy') in word:
        return 'easy'
    elif 'effective' in word:
        return 'effective'
    elif 'efficien' in word:
        return 'efficient'
    elif 'empower' in word:
        return 'empower'
    elif 'enabl' in word:
        return 'enable'
    elif 'encourag' in word:
        return 'encourage'
    elif 'enhanc' in word:
        return 'enhance'
    elif 'enjoy' in word:
        return 'enjoy'
    elif 'enthusia' in word:
        return 'enthusiasm'
    elif 'excellen' in word:
        return 'excellent'
    elif 'excel' in word:
        return 'excel'
    elif 'exceptional' in word:
        return 'exceptional'
    elif 'excit' in word:
        return 'exciting'
    elif 'exclusiv' in word:
        return 'exclusive'
    elif 'exemplary' in word:
        return 'exemplary'


def word_filter_fgh(word):
    if 'fail' in word:
        return 'fail'
    elif 'fallout' in word:
        return 'fallout'
    elif 'fals' in word:
        return 'false'
    elif 'fatal' in word:
        return 'fatal'
    elif 'fault' in word:
        return 'fault'
    elif 'fear' in word:
        return 'fear'
    elif 'felon' in word:
        return 'felony'
    elif 'fictitious' in word:
        return 'fictitious'
    elif 'fine' in word:
        return 'fine'
    elif ('fired' or 'firing') in word:
        return 'firing'
    elif 'flaw' in word:
        return 'flaw'
    elif 'forbid' in word:
        return 'forbid'
    elif 'forc' in word:
        return 'force'
    elif 'foreclos' in word:
        return 'foreclose'
    elif 'forego' in word:
        return 'forego'
    elif 'forestall' in word:
        return 'forestall'
    elif 'forfeit' in word:
        return 'forfeit'
    elif 'forger' in word:
        return 'forger'
    elif 'fraud' in word:
        return 'fraud'
    elif 'frivolous' in word:
        return 'frivolous'
    elif 'frustrat' in word:
        return 'frustrate'
    elif 'fugitive' in word:
        return 'fugitive'
    elif 'fantastic' in word:
        return 'fantastic'
    elif 'favorite' in word:
        return 'favorite'
    elif 'favor' in word:
        return 'favored'
    elif 'friendly' in word:
        return 'friendly'
    elif 'gratuitous' in word:
        return 'gratuitous'
    elif 'grievance' in word:
        return 'grievance'
    elif 'grossly' in word:
        return 'grossly'
    elif 'groundless' in word:
        return 'groundless'
    elif 'guilty' in word:
        return 'guilty'
    elif 'gain' in word:
        return 'gain'
    elif 'good' in word:
        return 'good'
    elif 'great' in word:
        return 'great'
    elif ('happy' or 'happi') in word:
        return 'happy'
    elif 'highest' in word:
        return 'highest'
    elif 'honor' in word:
        return 'honor'
    elif 'halt' in word:
        return 'halt'
    elif 'hamper' in word:
        return 'hamper'
    elif 'harass' in word:
        return 'harass'
    elif 'hardship' in word:
        return 'hardship'
    elif 'harm' in word:
        return 'harm'
    elif 'harsh' in word:
        return 'harsh'
    elif 'hazard' in word:
        return 'hazard'
    elif 'hinder' in word:
        return 'hinder'
    elif 'hostil' in word:
        return 'hostile'
    elif 'hurt' in word:
        return 'hurt'


def word_filter_i(word):
    if 'idl' in word:
        return 'idle'
    elif 'ignor' in word:
        return 'ignore'
    elif 'illegal' in word:
        return 'illegal'
    elif 'illegible' in word:
        return 'illegible'
    elif 'illicit' in word:
        return 'illicit'
    elif 'illiquid' in word:
        return 'illiquid'
    elif 'ill' in word:
        return 'ill'
    elif 'imbalance' in word:
        return 'imbalance'
    elif 'immature' in word:
        return 'immature'
    elif 'immoral' in word:
        return 'immoral'
    elif 'impair' in word:
        return 'impair'
    elif 'impasse' in word:
        return 'impasse'
    elif 'imped' in word:
        return 'impede'
    elif 'imperative' in word:
        return 'imperative'
    elif 'imperfection' in word:
        return 'imperfection'
    elif 'imperil' in word:
        return 'imperil'
    elif 'impermissible' in word:
        return 'impermissible'
    elif 'implicat' in word:
        return 'implicate'
    elif 'impossibl' in word:
        return 'impossible'
    elif 'impound' in word:
        return 'impound'
    elif 'impractic' in word:
        return 'impractical'
    elif 'imprisonment' in word:
        return 'imprisonment'
    elif 'improper' in word:
        return 'improper'
    elif 'improprieties' in word:
        return 'impropriety'
    elif 'imprudent' in word:
        return 'imprudent'
    elif 'inability' in word:
        return 'inability'
    elif 'inaccessible' in word:
        return 'inaccessible'
    elif 'inaccura' in word:
        return 'inaccuracy'
    elif 'inaction' in word:
        return 'inaction'
    elif 'inactivat' in word:
        return 'inactivate'
    elif 'inadequate' in word:
        return 'inadequat'
    elif 'inadvertent' in word:
        return 'inadvertent'
    elif 'inadvisable' in word:
        return 'inadvisable'
    elif 'inappropriate' in word:
        return 'inappropriate'
    elif 'inattention' in word:
        return 'inattention'
    elif 'incapable' in word:
        return 'incapable'
    elif 'incapacit' in word:
        return 'incapacity'
    elif 'incarcerat' in word:
        return 'incarcerate'
    elif 'inciden' in word:
        return 'incidence'
    elif 'incompatibl' in word:
        return 'incompatible'
    elif 'incompeten' in word:
        return 'incompetent'
    elif 'incomplete' in word:
        return 'incomplete'
    elif 'inconclusive' in word:
        return 'inconclusive'
    elif 'inconsisten' in word:
        return 'inconsistent'
    elif 'inconvenien' in word:
        return 'inconvenient'
    elif 'incorrect' in word:
        return 'incorrect'
    elif 'indecen' in word:
        return 'indecent'
    elif 'indefeasibl' in word:
        return 'indefeasible'
    elif 'indict' in word:
        return 'indict'
    elif 'ineffective' in word:
        return 'ineffective'
    elif 'inefficien' in word:
        return 'inefficient'
    elif 'ineligibl' in word:
        return 'ineligible'
    elif 'inequit' in word:
        return 'inequity'
    elif 'inevitable' in word:
        return 'inevitable'
    elif 'inexperience' in word:
        return 'inexperience'
    elif 'inferior' in word:
        return 'inferior'
    elif 'inflicted' in word:
        return 'inflicted'
    elif 'infraction' in word:
        return 'infraction'
    elif 'infring' in word:
        return 'infringe'
    elif 'inhibit' in word:
        return 'inhibit'
    elif 'inimical' in word:
        return 'inimical'
    elif 'injunction' in word:
        return 'injunction'
    elif 'injur' in word:
        return 'injure'
    elif 'inordinate' in word:
        return 'inordinate'
    elif 'inquiry' in word:
        return 'inquiry'
    elif 'insecure' in word:
        return 'insecure'
    elif 'insensitive' in word:
        return 'insensitive'
    elif 'insolven' in word:
        return 'insolvent'
    elif 'instability' in word:
        return 'instability'
    elif 'insubordination' in word:
        return 'insubordination'
    elif 'insufficien' in word:
        return 'insufficient'
    elif 'insurrection' in word:
        return 'insurrection'
    elif 'intentional' in word:
        return 'intentional'
    elif 'interfer' in word:
        return 'interfere'
    elif 'intermittent' in word:
        return 'intermittent'
    elif 'interrupt' in word:
        return 'interrupt'
    elif 'intimidation' in word:
        return 'intimidation'
    elif 'intrusion' in word:
        return 'intrusion'
    elif 'invalid' in word:
        return 'invalid'
    elif 'investigat' in word:
        return 'investigate'
    elif 'involuntar' in word:
        return 'involuntary'
    elif 'irreconcilabl' in word:
        return 'irreconcilable'
    elif 'irrecoverabl' in word:
        return 'irrecoverable'
    elif 'irregular' in word:
        return 'irregular'
    elif 'irreparabl' in word:
        return 'irreparable'
    elif 'irreversibl' in word:
        return 'irreversible'
    elif 'ideal' in word:
        return 'ideal'
    elif 'impress' in word:
        return 'impress'
    elif 'improv' in word:
        return 'improve'
    elif 'incredibl' in word:
        return 'incredible'
    elif 'influential' in word:
        return 'influential'
    elif 'informative' in word:
        return 'informative'
    elif 'ingenuity' in word:
        return 'ingenuity'
    elif 'innovat' in word:
        return 'innovate'
    elif 'insightful' in word:
        return 'insightful'
    elif 'inspiration' in word:
        return 'inspiration'
    elif 'integrity' in word:
        return 'integrity'
    elif 'invent' in word:
        return 'invent'


def word_filter_jklm(word):
    if 'jeopardize' in word:
        return 'jeopardize'
    elif 'justifiable' in word:
        return 'justifiable'
    elif 'kickback' in word:
        return 'kickback'
    elif 'knowingly' in word:
        return 'knowingly'
    elif 'lackluster' in word:
        return 'lackluster'
    elif 'lack' in word:
        return 'lack'
    elif 'lag' in word:
        return 'lag'
    elif 'laps' in word:
        return 'lapse'
    elif 'late' in word:
        return 'late'
    elif 'laundering' in word:
        return 'laundering'
    elif 'layoff' in word:
        return 'layoff'
    elif ('lie' or 'lying') in word:
        return 'lie'
    elif 'limitation' in word:
        return 'limitation'
    elif 'lingering' in word:
        return 'lingering'
    elif 'liquidat' in word:
        return 'liquidate'
    elif 'litigant' in word:
        return 'litigant'
    elif 'litigat' in word:
        return 'litigate'
    elif 'lockout' in word:
        return 'lockout'
    elif ('lose' or 'losing') in word:
        return 'lose'
    elif 'loss' in word:
        return 'loss'
    elif 'lost' in word:
        return 'lost'
    elif 'leadership' in word:
        return 'leadership'
    elif 'leading' in word:
        return 'leading'
    elif 'loyal' in word:
        return 'loyal'
    elif 'lucrative' in word:
        return 'lucrative'
    elif 'malfeasance' in word:
        return 'malfeasance'
    elif 'malfunction' in word:
        return 'malfunction'
    elif 'malic' in word:
        return 'malice'
    elif 'malpractice' in word:
        return 'malpractice'
    elif 'manipulat' in word:
        return 'manipulate'
    elif 'markdown' in word:
        return 'markdown'
    elif 'misapplication' in word:
        return 'misapplication'
    elif 'misappl' in word:
        return 'misapply'
    elif 'misappropriat' in word:
        return 'misappropriate'
    elif 'misbrand' in word:
        return 'misbranded'
    elif 'miscalculat' in word:
        return 'miscalculate'
    elif 'mischaracterization' in word:
        return 'mischaracterization'
    elif 'mischief' in word:
        return 'mischief'
    elif 'misclassification' in word:
        return 'misclassification'
    elif 'misclassif' in word:
        return 'misclassify'
    elif 'miscommunication' in word:
        return 'miscommunication'
    elif 'misconduct' in word:
        return 'misconduct'
    elif 'misdated' in word:
        return 'misdated'
    elif 'misdemeanor' in word:
        return 'misdemeanor'
    elif 'misdirect' in word:
        return 'misdirect'
    elif 'mishandl' in word:
        return 'mishandle'
    elif 'misinform' in word:
        return 'misinform'
    elif 'misinterpret' in word:
        return 'misinterpret'
    elif 'misjudg' in word:
        return 'misjudge'
    elif 'mislabel' in word:
        return 'mislabel'
    elif ('mislead' or 'misled') in word:
        return 'mislead'
    elif 'mismanag' in word:
        return 'mismanage'
    elif 'mismatch' in word:
        return 'mismatch'
    elif 'misplace' in word:
        return 'misplace'
    elif 'mispric' in word:
        return 'misprice'
    elif 'misrepresent' in word:
        return 'misrepresent'
    elif 'misstat' in word:
        return 'misstate'
    elif 'misstep' in word:
        return 'misstep'
    elif 'mistak' in word:
        return 'mistake'
    elif 'miss' in word:
        return 'miss'
    elif 'mistrial' in word:
        return 'mistrial'
    elif 'misunderst' in word:
        return 'misunderstand'
    elif 'misus' in word:
        return 'misuse'
    elif 'monopol' in word:
        return 'monopoly'
    elif 'morator' in word:
        return 'moratorium'
    elif 'mothball' in word:
        return 'mothball'
    elif 'meritorious' in word:
        return 'meritorious'


def word_filter_no(word):
    if 'negative' in word:
        return 'negative'
    elif ('neglect' or 'negligen') in word:
        return 'neglect'
    elif 'nonattainment' in word:
        return 'nonattainment'
    elif 'noncompetitive' in word:
        return 'noncompetitive'
    elif 'noncompl' in word:
        return 'noncompliant'
    elif 'nonconform' in word:
        return 'nonconformity'
    elif 'nondisclosure' in word:
        return 'nondisclosure'
    elif 'nonfunctional' in word:
        return 'nonfunctional'
    elif 'nonpayment' in word:
        return 'nonpayment'
    elif 'nonperform' in word:
        return 'nonperform'
    elif 'nonproduc' in word:
        return 'nonproductive'
    elif 'nonrecoverable' in word:
        return 'nonrecoverable'
    elif 'nonrenewal' in word:
        return 'nonrenewal'
    elif 'nuisance' in word:
        return 'nuisance'
    elif 'nullif' in word:
        return 'nullify'
    elif 'object' in word:
        return 'object'
    elif 'obscen' in word:
        return 'obscene'
    elif 'obsole' in word:
        return 'obsolete'
    elif 'obstacle' in word:
        return 'obstacle'
    elif 'obstruct' in word:
        return 'obstruct'
    elif 'offen' in word:
        return 'offence'
    elif ('omission' or 'omit') in word:
        return 'omit'
    elif 'onerous' in word:
        return 'onerous'
    elif 'opportunistic' in word:
        return 'opportunistic'
    elif 'oppos' in word:
        return 'oppose'
    elif 'opposition' in word:
        return 'opposition'
    elif 'outage' in word:
        return 'outage'
    elif 'outdate' in word:
        return 'outdate'
    elif 'outmoded' in word:
        return 'outmoded'
    elif 'overage' in word:
        return 'overage'
    elif ('overbuild' or 'overbuilt') in word:
        return 'overbuild'
    elif 'overburden' in word:
        return 'overburden'
    elif 'overcapacit' in word:
        return 'overcapacity'
    elif 'overcharg' in word:
        return 'overcharge'
    elif 'overcom' in word:
        return 'overcome'
    elif 'overdue' in word:
        return 'overdue'
    elif 'overestimat' in word:
        return 'overestimate'
    elif 'overload' in word:
        return 'overload'
    elif 'overlook' in word:
        return 'overlook'
    elif 'overpa' in word:
        return 'overpay'
    elif 'overproduc' in word:
        return 'overproduce'
    elif 'overrun' in word:
        return 'overrun'
    elif 'overshadow' in word:
        return 'overshadow'
    elif 'overstat' in word:
        return 'overstate'
    elif 'oversuppl' in word:
        return 'oversupply'
    elif 'overtly' in word:
        return 'overtly'
    elif 'overturn' in word:
        return 'overturn'
    elif 'overvalu' in word:
        return 'overvalue'
    elif 'opportunit' in word:
        return 'opportunity'
    elif 'optimistic' in word:
        return 'optimistic'
    elif 'outperform' in word:
        return 'outperform'
    elif 'perfect' in word:
        return 'perfect'
    elif 'pleasant' in word:
        return 'pleasant'
    elif 'pleased' in word:
        return 'pleased'
    elif 'pleasure' in word:
        return 'pleasure'
    elif 'plentiful' in word:
        return 'plentiful'
    elif 'popular' in word:
        return 'popular'
    elif 'positive' in word:
        return 'positive'
    elif 'preeminen' in word:
        return 'preeminent'
    elif 'premier' in word:
        return 'premier'
    elif 'premiere' in word:
        return 'premiere'
    elif 'prestig' in word:
        return 'prestige'
    elif 'proactive' in word:
        return 'proactive'
    elif 'proficien' in word:
        return 'proficient'
    elif 'profitab' in word:
        return 'profitable'
    elif 'progress' in word:
        return 'progress'
    elif 'prosper' in word:
        return 'prospers'


def word_filter_pq(word):
    if 'panic' in word:
        return 'panic'
    elif 'penaliz' in word:
        return 'penalize'
    elif 'penalt' in word:
        return 'penalty'
    elif 'peril' in word:
        return 'peril'
    elif 'perjury' in word:
        return 'perjury'
    elif 'perpetrat' in word:
        return 'perpetrate'
    elif 'persist' in word:
        return 'persist'
    elif 'pervasive' in word:
        return 'pervasive'
    elif 'petty' in word:
        return 'petty'
    elif 'picket' in word:
        return 'picket'
    elif 'plaintiff' in word:
        return 'plaintiff'
    elif ('plea' or 'pled') in word:
        return 'plead'
    elif 'poor' in word:
        return 'poor'
    elif ('poses' or 'posing') in word:
        return 'pose'
    elif 'postpon' in word:
        return 'postpone'
    elif 'precipitated' in word:
        return 'precipitated'
    elif 'precipitous' in word:
        return 'precipitous'
    elif 'preclud' in word:
        return 'preclude'
    elif 'predatory' in word:
        return 'predatory'
    elif 'prejudic' in word:
        return 'prejudice'
    elif 'prematur' in word:
        return 'premature'
    elif 'pressing' in word:
        return 'pressing'
    elif 'pretrial' in word:
        return 'pretrial'
    elif 'prevent' in word:
        return 'prevent'
    elif 'problem' in word:
        return 'problem'
    elif 'prolong' in word:
        return 'prolong'
    elif 'prone' in word:
        return 'prone'
    elif 'prosecut' in word:
        return 'prosecute'
    elif 'protest' in word:
        return 'protest'
    elif 'protract' in word:
        return 'protracted'
    elif 'provok' in word:
        return 'provoke'
    elif 'punish' in word:
        return 'punish'
    elif 'punitive' in word:
        return 'punitive'
    elif 'purport' in word:
        return 'purport'
    elif 'question' in word:
        return 'question'
    elif 'quit' in word:
        return 'quit'


def word_filter_rs(word):
    if 'racketeer' in word:
        return 'racketeer'
    elif 'rationaliz' in word:
        return 'rationalize'
    elif 'reassessment' in word:
        return 'reassessment'
    elif 'reassign' in word:
        return 'reassign'
    elif 'recall' in word:
        return 'recall'
    elif 'recession' in word:
        return 'recession'
    elif 'reckless' in word:
        return 'reckless'
    elif 'redact' in word:
        return 'redact'
    elif 'redefault' in word:
        return 'redefault'
    elif 'redress' in word:
        return 'redress'
    elif 'refus' in word:
        return 'refusal'
    elif 'reject' in word:
        return 'reject'
    elif 'relinquish' in word:
        return 'relinquish'
    elif 'reluctan' in word:
        return 'reluctant'
    elif 'renegotiat' in word:
        return 'renegotiate'
    elif 'renounc' in word:
        return 'renounce'
    elif 'reparation' in word:
        return 'reparation'
    elif 'repossess' in word:
        return 'repossess'
    elif 'repudiat' in word:
        return 'repudiate'
    elif 'resign' in word:
        return 'resign'
    elif 'restat' in word:
        return 'restate'
    elif 'restructur' in word:
        return 'restructure'
    elif 'retaliat' in word:
        return 'retaliate'
    elif 'retribution' in word:
        return 'retribution'
    elif ('revocation' or 'revok') in word:
        return 'revocation'
    elif 'ridicul' in word:
        return 'ridicule'
    elif ('risky' or 'riskie') in word:
        return 'risky'
    elif 'rebound' in word:
        return 'rebound'
    elif 'receptive' in word:
        return 'receptive'
    elif 'regain' in word:
        return 'regain'
    elif 'resolve' in word:
        return 'resolve'
    elif 'revolutioniz' in word:
        return 'revolutionize'
    elif 'reward' in word:
        return 'reward'
    elif 'sabotage' in word:
        return 'sabotage'
    elif 'sacrific' in word:
        return 'sacrifice'
    elif 'scandal' in word:
        return 'scandal'
    elif ('scrutiniz' or 'scrutiny') in word:
        return 'scrutinize'
    elif 'secrecy' in word:
        return 'secrecy'
    elif 'seiz' in word:
        return 'seize'
    elif 'sentenc' in word:
        return 'sentence'
    elif 'serious' in word:
        return 'serious'
    elif 'setback' in word:
        return 'setback'
    elif ('severe' or 'severit') in word:
        return 'severe'
    elif 'sever' in word:
        return 'sever'
    elif 'sharply' in word:
        return 'sharply'
    elif 'shocked' in word:
        return 'shocked'
    elif 'shortage' in word:
        return 'shortage'
    elif 'shortfall' in word:
        return 'shortfall'
    elif 'shrinkage' in word:
        return 'shrinkage'
    elif 'shutdown' in word:
        return 'shutdown'
    elif ('shut' or 'shutting') in word:
        return 'shut'
    elif 'slander' in word:
        return 'slander'
    elif 'slippage' in word:
        return 'slippage'
    elif 'slowdown' in word:
        return 'slowdown'
    elif 'slow' in word:
        return 'slow'
    elif 'sluggish' in word:
        return 'sluggish'
    elif 'solvenc' in word:
        return 'solvency'
    elif 'spam' in word:
        return 'spam'
    elif 'staggering' in word:
        return 'staggering'
    elif 'stagn' in word:
        return 'stagnate'
    elif 'standstill' in word:
        return 'standstill'
    elif 'stolen' in word:
        return 'stolen'
    elif 'stop' in word:
        return 'stop'
    elif 'strain' in word:
        return 'strain'
    elif 'stress' in word:
        return 'stress'
    elif 'stringent' in word:
        return 'stringent'
    elif ('subjected' or 'subjecting' or 'subjection') in word:
        return 'subjected'
    elif 'subpoena' in word:
        return 'subpoena'
    elif 'substandard' in word:
        return 'substandard'
    elif ('sue' or 'suing') in word:
        return 'sue'
    elif 'suffer' in word:
        return 'suffer'
    elif 'summon' in word:
        return 'summon'
    elif 'susceptib' in word:
        return 'susceptible'
    elif 'suspect' in word:
        return 'suspect'
    elif 'suspen' in word:
        return 'suspend'
    elif 'suspicion' in word:
        return 'suspicion'
    elif ('satisfact' or 'satisf') in word:
        return 'satisfy'
    elif 'smooth' in word:
        return 'smooth'
    elif 'solv' in word:
        return 'solves'
    elif 'spectacular' in word:
        return 'spectacular'
    elif ('stable' or 'stability' or 'stabiliz') in word:
        return 'stable'
    elif 'strength' in word:
        return 'strength'
    elif 'strong' in word:
        return 'strong'
    elif ('success' or 'succeed') in word:
        return 'success'
    elif 'superior' in word:
        return 'superior'
    elif 'surpass' in word:
        return 'surpass'
    elif 'transparency' in word:
        return 'transparency'
    elif 'tremendous' in word:
        return 'tremendous'


def word_filter_t(word):
    if 'taint' in word:
        return 'taint'
    elif 'tampered' in word:
        return 'tampered'
    elif 'tense' in word:
        return 'tense'
    elif 'terminat' in word:
        return 'terminate'
    elif 'testify' in word:
        return 'testify'
    elif 'threat' in word:
        return 'threat'
    elif 'tighten' in word:
        return 'tighten'
    elif 'tolerat' in word:
        return 'tolerate'
    elif 'tortuous' in word:
        return 'tortuous'
    elif 'traged' in word:
        return 'tragedy'
    elif 'tragic' in word:
        return 'tragic'
    elif 'traumatic' in word:
        return 'traumatic'
    elif 'trouble' in word:
        return 'trouble'
    elif 'turbulence' in word:
        return 'turbulence'
    elif 'turmoil' in word:
        return 'turmoil'


def word_filter_u(word):
    if 'unable' in word:
        return 'unable'
    elif 'unacceptabl' in word:
        return 'unacceptable'
    elif 'unaccounted' in word:
        return 'unaccounted'
    elif 'unannounced' in word:
        return 'unannounced'
    elif 'unanticipated' in word:
        return 'unanticipated'
    elif 'unapproved' in word:
        return 'unapproved'
    elif 'unattractive' in word:
        return 'unattractive'
    elif 'unauthorized' in word:
        return 'unauthorized'
    elif 'unavailabl' in word:
        return 'unavailable'
    elif 'unavoidabl' in word:
        return 'unavoidable'
    elif 'unaware' in word:
        return 'unaware'
    elif 'uncollect' in word:
        return 'uncollect'
    elif 'uncollectibil' in word:
        return 'uncontrollable'
    elif 'uncompetitive' in word:
        return 'uncompetitive'
    elif 'uncompleted' in word:
        return 'uncompleted'
    elif 'unconscionabl' in word:
        return 'unconscionable'
    elif 'uncontrol' in word:
        return 'uncontrolled'
    elif 'uncorrected' in word:
        return 'uncorrected'
    elif 'uncover' in word:
        return 'uncover'
    elif 'undeliver' in word:
        return 'undeliver'
    elif 'undercapitalized' in word:
        return 'undercapitalized'
    elif 'undercut' in word:
        return 'undercut'
    elif 'underestimat' in word:
        return 'underestimate'
    elif 'underfunded' in word:
        return 'underfunded'
    elif 'underinsured' in word:
        return 'underinsured'
    elif 'undermin' in word:
        return 'undermine'
    elif ('underpaid' or 'underpayment' or 'underpay') in word:
        return 'underpay'
    elif 'underperform' in word:
        return 'underperform'
    elif 'underproduce' in word:
        return 'underproduce'
    elif 'underreporting' in word:
        return 'underreporting'
    elif 'understat' in word:
        return 'understate'
    elif 'underutilization' in word:
        return 'underutilization'
    elif 'undesir' in word:
        return 'undesirable'
    elif 'undetected' in word:
        return 'undetected'
    elif 'undetermined' in word:
        return 'undetermined'
    elif 'undisclosed' in word:
        return 'undisclosed'
    elif 'undocumented' in word:
        return 'undocumented'
    elif 'underutilized' in word:
        return 'underutilized'
    elif 'undu' in word:
        return 'undue'
    elif 'uneconomic' in word:
        return 'uneconomic'
    elif 'unemploy' in word:
        return 'unemploy'
    elif 'unethical' in word:
        return 'unethical'
    elif 'unethically' in word:
        return 'unethically'
    elif 'unexcused' in word:
        return 'unexcused'
    elif 'unexpected' in word:
        return 'unexpected'
    elif 'unexpectedly' in word:
        return 'unexpectedly'
    elif 'unfair' in word:
        return 'unfair'
    elif ('unfavorab' or 'unfavourab') in word:
        return 'unfavorable'
    elif 'unfeasible' in word:
        return 'unfeasible'
    elif 'unfit' in word:
        return 'unfit'
    elif ('unforeseen' or 'unforseen' or 'unforeseeable') in word:
        return 'unforeseen'
    elif 'unfortunate' in word:
        return 'unfortunate'
    elif 'unfounded' in word:
        return 'unfounded'
    elif 'unfriendly' in word:
        return 'unfriendly'
    elif 'unfulfilled' in word:
        return 'unfulfilled'
    elif 'unfunded' in word:
        return 'unfunded'
    elif 'uninsured' in word:
        return 'uninsured'
    elif ('unintended' or 'unintentional') in word:
        return 'unintended'
    elif 'unjust' in word:
        return 'unjust'
    elif 'unknowing' in word:
        return 'unknowing'
    elif 'unlawful' in word:
        return 'unlawful'
    elif 'unlicensed' in word:
        return 'unlicensed'
    elif 'unliquidated' in word:
        return 'unliquidated'
    elif 'unmarketable' in word:
        return 'unmarketable'
    elif 'unmerchantable' in word:
        return 'unmerchantable'
    elif 'unmeritorious' in word:
        return 'unmeritorious'
    elif 'unnecessar' in word:
        return 'unnecessary'
    elif 'unneeded' in word:
        return 'unneeded'
    elif 'unobtainable' in word:
        return 'unobtainable'
    elif 'unoccupied' in word:
        return 'unoccupied'
    elif 'unpaid' in word:
        return 'unpaid'
    elif 'unrecover' in word:
        return 'unrecovered'
    elif 'unreimbursed' in word:
        return 'unreimbursed'
    elif 'unreliable' in word:
        return 'unreliable'
    elif 'unremedied' in word:
        return 'unremedied'
    elif 'unsafe' in word:
        return 'unsafe'
    elif 'unrest' in word:
        return 'unrest'
    elif 'unresolved' in word:
        return 'unresolved'
    elif 'unreported' in word:
        return 'unreported'
    elif 'unperformed' in word:
        return 'unperformed'
    elif 'unplanned' in word:
        return 'unplanned'
    elif 'unpopular' in word:
        return 'unpopular'
    elif 'unpredict' in word:
        return 'unpredictable'
    elif 'unproductive' in word:
        return 'unproductive'
    elif 'unprofitabl' in word:
        return 'unprofitabl'
    elif 'unqualified' in word:
        return 'unqualified'
    elif 'unrealistic' in word:
        return 'unrealistic'
    elif 'unreasonabl' in word:
        return 'unreasonable'
    elif 'unreceptive' in word:
        return 'unreceptive'
    elif 'unsuccessful' in word:
        return 'unsuccessful'
    elif 'unsubstantiated' in word:
        return 'unsubstantiated'
    elif 'unstable' in word:
        return 'unstable'
    elif 'unstabilized' in word:
        return 'unstabilized'
    elif 'unsound' in word:
        return 'unsound'
    elif 'unsold' in word:
        return 'unsold'
    elif 'unsellable' in word:
        return 'unsellable'
    elif 'unscheduled' in word:
        return 'unscheduled'
    elif 'unsavory' in word:
        return 'unsavory'
    elif 'unsatisf' in word:
        return 'unsatisfied'
    elif 'unsal' in word:
        return 'unsalable'
    elif 'unsuitabl' in word:
        return 'unsuitable'
    elif 'unsuitab' in word:
        return 'unsuitable'
    elif 'unsuited' in word:
        return 'unsuited'
    elif 'unsure' in word:
        return 'unsure'
    elif 'unsuspect' in word:
        return 'unsuspected'
    elif 'unsustainable' in word:
        return 'unsustainable'
    elif 'untenable' in word:
        return 'untenable'
    elif 'untimely' in word:
        return 'untimely'
    elif 'untrusted' in word:
        return 'untrusted'
    elif 'untruth' in word:
        return 'untruth'
    elif 'unusable' in word:
        return 'unusable'
    elif 'unwanted' in word:
        return 'unwanted'
    elif 'unwarranted' in word:
        return 'unwarranted'
    elif 'unwelcome' in word:
        return 'unwelcome'
    elif 'unwilling' in word:
        return 'unwilling'
    elif 'upset' in word:
        return 'upset'
    elif 'urgen' in word:
        return 'urgent'
    elif 'usurious' in word:
        return 'usurious'
    elif 'usurp' in word:
        return 'usurp'
    elif 'usury' in word:
        return 'usury'
    elif 'unmatched' in word:
        return 'unmatched'
    elif 'unparalleled' in word:
        return 'unparalleled'
    elif 'unsurpassed' in word:
        return 'unsurpassed'
    elif 'upturn' in word:
        return 'upturn'


def word_filter_vw(word):
    if 'vandalism' in word:
        return 'vandalism'
    elif 'verdict' in word:
        return 'verdict'
    elif 'vetoed' in word:
        return 'vetoed'
    elif 'victims' in word:
        return 'victims'
    elif 'violat' in word:
        return 'violate'
    elif 'violen' in word:
        return 'violent'
    elif 'vitiat' in word:
        return 'vitiate'
    elif 'void' in word:
        return 'voided'
    elif 'volatil' in word:
        return 'volatile'
    elif 'vulnerabl' in word:
        return 'vulnerable'
    elif 'warn' in word:
        return 'warn'
    elif ('wasted' or 'wasteful' or 'wasting') in word:
        return 'wasted'
    elif 'weak' in word:
        return 'weak'
    elif 'willfully' in word:
        return 'willfully'
    elif 'worr' in word:
        return 'worry'
    elif 'worse' in word:
        return 'worse'
    elif 'worst' in word:
        return 'worst'
    elif 'worthless' in word:
        return 'worthless'
    elif 'writedown' in word:
        return 'writedown'
    elif 'writeoff' in word:
        return 'writeoff'
    elif 'wrongdoing' in word:
        return 'wrongdoing'
    elif 'wrong' in word:
        return 'wrong'
    elif 'valuable' in word:
        return 'valuable'
    elif 'versatil' in word:
        return 'versatile'
    elif 'vibran' in word:
        return 'vibrant'
    elif 'win' in word:
        return 'win'
    elif 'worthy' in word:
        return 'worthy'
