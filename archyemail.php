require_once('./vendor/autoload.php');
use Postmark\PostmarkClient;
use Postmark\Models\PostmarkException;

try{
        $client = new PostmarkClient("4322111a-0d75-4777-8111-2d83f0664762");
    $sendResult = $client->sendEmail("a@deberker.com", 
        "a@deberker.com", 
        "Hello from Postmark!",
        "This is just a friendly 'hello' from your friends at Postmark.");

}catch(PostmarkException $ex){
    // If client is able to communicate with the API in a timely fashion,
    // but the message data is invalid, or there's a server error,
    // a PostmarkException can be thrown.
    echo $ex->httpStatusCode;
    echo $ex->message;
    echo $ex->postmarkApiErrorCode;

}catch(Exception $generalException){
    // A general exception is thown if the API
    // was unreachable or times out.
}