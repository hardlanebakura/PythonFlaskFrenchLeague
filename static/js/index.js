qualificationRanks = document.getElementsByClassName("qualificationsranks_11")

qualificationRanks[0].style.backgroundColor = "#4285F4";
qualificationRanks[1].style.backgroundColor = "#FA7B17";
qualificationRanks[2].style.backgroundColor = "#34A853";
qualificationRanks[3].style.backgroundColor = "#FBBC04";
qualificationRanks[4].style.backgroundColor = "#EA4335";

league_1 = document.getElementsByClassName("league_1");

for(let i = 0; i < league_1.length; i++) {

league_1[i].addEventListener("mouseover", event => {

league_1[i].style.backgroundColor = "aquamarine";

})

}

for(let i = 0; i < league_1.length; i++) {

league_1[i].addEventListener("mouseout", event => {

league_1[i].style.backgroundColor = "#fff";

})

}

