var teamsTeamImages = document.getElementsByTagName("img");
var allTrophiesHeaders = document.getElementsByClassName("all_trophies_header");
var allTrophiesForCompetition = document.getElementsByClassName("all_trophies_trophies");
var trophies = document.getElementsByClassName("trophy");
var teamTrophiesImages = document.getElementsByClassName("team_trophy_img");

const refactorName = (name) => {
    return name.replaceAll(" ", "-");
}

for (let i = 0; i < teamTrophiesImages.length; i++) {

    console.log(teamTrophiesImages[i].parentNode.parentNode.parentNode.childNodes[1].innerHTML);
    var competitionName = refactorName(teamTrophiesImages[i].parentNode.parentNode.parentNode.childNodes[1].innerText);
    console.log(competitionName);
    teamTrophiesImages[i].setAttribute("src", `/./static/images/trophies/${competitionName}.jpg`);

}

console.log(team);

var teamName = refactorName(team);
console.log(teamName);
teamsTeamImages[10].setAttribute("src", `/./static/images/stadiums/stadium-${teamName}.jpg`);



