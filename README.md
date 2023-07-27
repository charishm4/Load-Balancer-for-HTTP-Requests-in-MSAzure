# Load Balancer for HTTP Requests in MSAzure
  Implementation and Demonstration of Load Balancer for HTTP Requests in MS Azure using Virtualization Techniques. 
  
 **Web service:** \
• Implemented a web service that displays a webpage upon request by the client. \
• The service is provided by two or more different web servers (server 2, server 3, etc.), and the servers.
will answer according to the selected load balancing scheme(round robin(RR), weighted round robin(WRR), load sensitivity(LS)). \
• There is a proxy (server 1) on the ingress. 

**Web servers:** \
• Each web server provides a similar webpage but the response indicates which server is used. \
• The web server will send spontaneously updates about their load status to the load balancer. \
• The load balancer implements have different adaptation strategies: RR/WRR/LS. \
• The load balancer receives all HTTPS requests from the proxy and forwards them to the appropriate web server according to the applied balancing scheme. \
• The load balancer forms a “queue” for each web server. 

**Usage Example:** \
Build docker image for respective load balancing technique on server 1: \
docker build -t rr . \ 
docker run -p 8080:8080 rr \

Build docker image for the Python app on server 2 and server 3: \
docker build -t pymyweb . \
docker run -p 8080:8080 pymyweb 
