batch: for error in 64 go to 32
- more the batch is more computation required
- step 1. `max_batch = number of classes * 2000`
- step 2. `step = (80% of max_batch), (90% of max_batch)`
- step 3. `filter = (number of classes + 5 ) * 3`
