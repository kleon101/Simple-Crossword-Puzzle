// JavaScript for the Basketball LiveStat Project - SV

//Initialsing variables for the different stats to 0
let points = 0
let rebounds = 0
let assists = 0
let steals = 0
let blocks = 0
let turnovers = 0

//Getting the html elements
let ptsEl = document.getElementById("points-el")
let rebEl = document.getElementById("rebounds-el")
let astEl = document.getElementById("assists-el")
let stlEl = document.getElementById("steals-el")
let blkEl = document.getElementById("blocks-el")
let tovEl = document.getElementById("turnovers-el")

let saveEl = document.getElementById("save-el")

//Creating functions that increments stat by 1 when button is clicked
function addPoint() {
    points += 1
    ptsEl.textContent = points
}
function addRebound() {
    rebounds += 1
    rebEl.textContent = rebounds
}
function addAssist() {
    assists += 1
    astEl.textContent = assists
}
function addSteal() {
    steals += 1
    stlEl.textContent = steals
}
function addBlock() {
    blocks += 1
    blkEl.textContent = blocks
}
function addTurnover() {
    turnovers += 1
    tovEl.textContent = turnovers
}

//Function which resets the stat
function setToZero(stat) {
    stat.textContent = 0
    stat = 0
}
//Creating function to save the statline in presentable format
function save() {
    saveEl.textContent = "Final Statline: pts - " + points + " / reb - " + rebounds + 
    " / ast - " + assists + " / stl - " + steals + " / blk - " + blocks + " / tov - " + turnovers

    //Setting all the stats back to zero after save is clicked
    setToZero(ptsEl)
    setToZero(rebEl)
    setToZero(astEl)
    setToZero(stlEl)
    setToZero(blkEl)
    setToZero(tovEl)
}