export default function taskBlock(trueOrFalse) {
        const task = false;
        const task2 = true;
  
    if (trueOrFalse) {
        const taskUp = true;
        const task2Up = false;
        return [taskUp, task2Up];
    }
  
    return [task, task2];
  }
