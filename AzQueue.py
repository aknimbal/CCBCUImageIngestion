from azure.storage.queue import QueueService

#constructor
def load(azureQueueAccountName,azureQueueKey,azureQueueAnalysisResults):
    queue_service = QueueService(account_name=azureQueueAccountName, account_key=azureQueueKey)
    #create queue if doesnt exist
    if not queue_service.exists(azureQueueAnalysisResults):
        queue_service.create_queue(azureQueueAnalysisResults)
    return queue_service
    
#process messages 
def put_in_queue(queue_service,azureQueueAnalysisResults,page_list):    
    for page in page_list:
        queue_service.put_message(azureQueueAnalysisResults, "{}".format(page), time_to_live=-1)

