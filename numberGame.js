// Number guessing game

const randomNumber= Math.floor(Math.random()*10)+1;

let guess;
let numberOfAttempts=0;

while (guess != randomNumber) {
    guess +=1
    
    if (numberOfAttempts<3){
        guess = Number(prompt("Enter a number between 1 and 10: "));
        console.log("Your guess:",guess);
        
        if (guess< randomNumber) {
            console.log("Too low! Try again.");
        }
        else if (guess > randomNumber){
            console.log("Too high! Try again.");
        }
        else if (guess== randomNumber){
            console.log(`Congratulations! You found it in ${numberOfAttempts} attempts!`);
        }
        else {
            console.log("Invalid input");
        }

    }
    if (numberOfAttempts==3 && guess != randomNumber){
        console.log("Game Over! You ran out of attempts. The number was "+randomNumber)
    }

    


}