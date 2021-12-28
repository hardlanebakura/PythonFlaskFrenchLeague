var teamsTeamOverviews = document.getElementsByClassName("teams_team_overview");
var teamsTeamName = document.getElementsByClassName("teams_team_name");
var teamsTeamImages = document.getElementsByTagName("img");
var t = Array.from(teamsTeamImages);
console.log(t.length);
t.splice(0, 10);
var teams_team_links = document.getElementsByTagName("a");
//for (let i = 0; i < t.length; i++) {
//    teams_team_links.push(t[i].getElementsByTagName("a"));
//}
var array_links = Array.from(teams_team_links);
array_links.splice(0, 4);
console.log(array_links);
for (let i = 0; i < array_links.length; i++) {
    console.log(array_links[i].getAttribute("href"));
}
console.log(teams_team_links.length);
teamsTeamImages = t;
console.log(t.length);
console.log(teamsTeamOverviews.length);
console.log(teamsTeamImages);
const team_names_to_lowercase = (team_name) => {

    var t = team_name.replaceAll(" ", "-");
    return t;

}

const moveElement = (element) => {

    if (element.length < 17) {
        let border = 41 + (16 - element.length)/2;
        return border;
        }
    return 40;

}

for (let i = 0; i < teamsTeamOverviews.length; i++) {

    console.log(teams[i].length);
    let teamNameLeft = moveElement(teams[i]);
    console.log(moveElement(teams[i]));
    teamsTeamName[i].style.left = `${teamNameLeft}%`;
    teamsTeamName[i].style.background = "none";
    var team_name = team_names_to_lowercase(teams[i]);
    console.log(team_name);
    t[i].setAttribute("src", `../static/images/stadiums/stadium-${team_name}.jpg`);
    //find link elements for selected node
    array_links[i].setAttribute("href", `/teams/${i + 1}`);
    //teams_team_links[i].setAttribute("href", "/teams/2");
}

