import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { 
  AlertTriangle, 
  CheckCircle2, 
  Clock, 
  ExternalLink,
  TrendingUp,
  Activity
} from "lucide-react";

const mockAlerts = [
  {
    id: 1,
    type: "high",
    title: "False vaccine information spreading",
    source: "Twitter, WhatsApp",
    impact: 94,
    status: "verified",
    time: "2 mins ago"
  },
  {
    id: 2,
    type: "medium",
    title: "Misleading political claim detected",
    source: "Facebook, Instagram",
    impact: 76,
    status: "processing",
    time: "5 mins ago"
  },
  {
    id: 3,
    type: "low",
    title: "Unverified news article shared",
    source: "Reddit",
    impact: 42,
    status: "flagged",
    time: "8 mins ago"
  }
];

const DashboardPreview = () => {
  return (
    <section className="py-24 px-4 bg-muted/30">
      <div className="container mx-auto max-w-7xl">
        {/* Section Header */}
        <div className="text-center mb-16 space-y-4">
          <h2 className="text-4xl md:text-5xl font-bold text-foreground">
            Real-Time Monitoring
          </h2>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
            Watch as our AI agents autonomously detect and verify misinformation across platforms
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
          {/* Live Stats */}
          <Card className="p-6 bg-gradient-card backdrop-blur-sm border-primary/10">
            <div className="flex items-start justify-between mb-4">
              <div>
                <p className="text-sm text-muted-foreground">Active Scans</p>
                <p className="text-3xl font-bold text-foreground mt-1">1,247</p>
              </div>
              <Activity className="w-8 h-8 text-primary animate-pulse-glow" />
            </div>
            <div className="flex items-center gap-2 text-sm text-success">
              <TrendingUp className="w-4 h-4" />
              <span>+12% from last hour</span>
            </div>
          </Card>

          <Card className="p-6 bg-gradient-card backdrop-blur-sm border-destructive/10">
            <div className="flex items-start justify-between mb-4">
              <div>
                <p className="text-sm text-muted-foreground">Flagged Content</p>
                <p className="text-3xl font-bold text-foreground mt-1">89</p>
              </div>
              <AlertTriangle className="w-8 h-8 text-destructive animate-pulse-glow" />
            </div>
            <div className="flex items-center gap-2 text-sm text-muted-foreground">
              <Clock className="w-4 h-4" />
              <span>24 high priority</span>
            </div>
          </Card>

          <Card className="p-6 bg-gradient-card backdrop-blur-sm border-success/10">
            <div className="flex items-start justify-between mb-4">
              <div>
                <p className="text-sm text-muted-foreground">Verified Today</p>
                <p className="text-3xl font-bold text-foreground mt-1">342</p>
              </div>
              <CheckCircle2 className="w-8 h-8 text-success" />
            </div>
            <div className="flex items-center gap-2 text-sm text-success">
              <CheckCircle2 className="w-4 h-4" />
              <span>99.2% accuracy</span>
            </div>
          </Card>
        </div>

        {/* Alerts Feed */}
        <Card className="p-8 bg-gradient-card backdrop-blur-sm border-primary/10">
          <div className="flex items-center justify-between mb-6">
            <h3 className="text-2xl font-semibold text-foreground">Recent Alerts</h3>
            <Badge variant="outline" className="animate-pulse-glow">
              Live
            </Badge>
          </div>

          <div className="space-y-4">
            {mockAlerts.map((alert) => (
              <div 
                key={alert.id}
                className="p-4 rounded-lg border bg-card hover:bg-accent/5 transition-colors"
              >
                <div className="flex items-start justify-between gap-4">
                  <div className="flex-1 space-y-2">
                    <div className="flex items-center gap-3">
                      <Badge 
                        variant={alert.type === 'high' ? 'destructive' : alert.type === 'medium' ? 'default' : 'secondary'}
                        className="uppercase text-xs"
                      >
                        {alert.type} priority
                      </Badge>
                      <span className="text-xs text-muted-foreground">{alert.time}</span>
                    </div>
                    <h4 className="font-semibold text-foreground">{alert.title}</h4>
                    <div className="flex items-center gap-4 text-sm text-muted-foreground">
                      <span>Source: {alert.source}</span>
                      <span>•</span>
                      <span className="flex items-center gap-1">
                        Impact Score: 
                        <span className={`font-semibold ${alert.impact > 80 ? 'text-destructive' : alert.impact > 60 ? 'text-warning' : 'text-muted-foreground'}`}>
                          {alert.impact}
                        </span>
                      </span>
                    </div>
                  </div>
                  <div className="flex items-center gap-2">
                    {alert.status === 'verified' && (
                      <Badge variant="outline" className="bg-success/10 text-success border-success/20">
                        <CheckCircle2 className="w-3 h-3 mr-1" />
                        Verified
                      </Badge>
                    )}
                    {alert.status === 'processing' && (
                      <Badge variant="outline" className="bg-warning/10 text-warning border-warning/20">
                        <Clock className="w-3 h-3 mr-1" />
                        Processing
                      </Badge>
                    )}
                    {alert.status === 'flagged' && (
                      <Badge variant="outline" className="bg-destructive/10 text-destructive border-destructive/20">
                        <AlertTriangle className="w-3 h-3 mr-1" />
                        Flagged
                      </Badge>
                    )}
                    <Button variant="ghost" size="sm">
                      <ExternalLink className="w-4 h-4" />
                    </Button>
                  </div>
                </div>
              </div>
            ))}
          </div>

          <div className="mt-6 text-center">
            <Button variant="outline">View All Alerts</Button>
          </div>
        </Card>
      </div>
    </section>
  );
};

export default DashboardPreview;
