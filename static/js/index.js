qualificationsranks_11 = document.getElementsByClassName("qualificationsranks_11")

console.log(qualificationsranks_11.length);

qualificationsranks_11[0].style.backgroundColor = "#4285F4";
qualificationsranks_11[1].style.backgroundColor = "#FA7B17";
qualificationsranks_11[2].style.backgroundColor = "#34A853";
qualificationsranks_11[3].style.backgroundColor = "#FBBC04";
qualificationsranks_11[4].style.backgroundColor = "#EA4335";

league_1 = document.getElementsByClassName("league_1");
console.log(document.getElementsByClassName("league_1").length);

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

