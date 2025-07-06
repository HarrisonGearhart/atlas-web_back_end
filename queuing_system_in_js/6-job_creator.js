import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Define the job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is the notification message',
};

// Create the job in the 'push_notification_code' queue
const job = queue.create('push_notification_code', jobData);

// Save the job and listen for lifecycle events
job
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed', () => {
    console.log('Notification job failed');
  });

