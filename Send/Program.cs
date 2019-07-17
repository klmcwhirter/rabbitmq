using System;
using System.Linq;
using System.Text;
using RabbitMQ.Client;

namespace Send
{
    class Program
    {
        public static void Main(string[] args)
        {
            var factory = new ConnectionFactory() { HostName = "localhost" };
            using (var connection = factory.CreateConnection())
            using (var channel = connection.CreateModel())
            {
                channel.QueueDeclare(queue: "hello", durable: false, exclusive: false, autoDelete: false, arguments: null);

                SendMessages(args, channel);
            }

            // Console.WriteLine(" Press [enter] to exit.");
            // Console.ReadLine();
        }

        private static void SendMessages(string[] args, IModel channel)
        {
            var greetee = args != null && args.Length > 0 && !string.IsNullOrWhiteSpace(args[0]) ? args[0] : "World";

            var count = Convert.ToInt32(args != null && args.Length > 1 && !string.IsNullOrWhiteSpace(args[1]) ? args[1] : "1");

            Enumerable.Range(0, count).ToList().ForEach(i => SendMessage(greetee, i, channel));
        }

        private static bool SendMessage(string greetee, int num, IModel channel)
        {
            var message = $"Hello {greetee} [{num}]!";
            var body = Encoding.UTF8.GetBytes(message);

            channel.BasicPublish(exchange: "", routingKey: "hello", basicProperties: null, body: body);
            Console.WriteLine(" [x] Sent {0}", message);

            return true;
        }
    }
}
