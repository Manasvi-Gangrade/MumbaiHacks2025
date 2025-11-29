import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { 
  Search, 
  Shield, 
  Bell, 
  Database,
  ArrowRight
} from "lucide-react";

const agents = [
  {
    id: 1,
    name: "Detection Agent",
    icon: Search,
    description: "Scans social media, news, and messaging platforms",
    status: "active",
    color: "text-primary"
  },
  {
    id: 2,
    name: "Verification Agent",
    icon: Shield,
    description: "Validates content against trusted sources using RAG",
    status: "active",
    color: "text-secondary"
  },
  {
    id: 3,
    name: "Impact Agent",
    icon: Database,
    description: "Calculates virality and severity scores",
    status: "active",
    color: "text-accent"
  },
  {
    id: 4,
    name: "Alert Agent",
    icon: Bell,
    description: "Sends real-time notifications to users",
    status: "active",
    color: "text-success"
  }
];

const AgentVisualization = () => {
  return (
    <section className="py-24 px-4 bg-background">
      <div className="container mx-auto max-w-7xl">
        {/* Section Header */}
        <div className="text-center mb-16 space-y-4">
          <h2 className="text-4xl md:text-5xl font-bold text-foreground">
            Multi-Agent System
          </h2>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
            Specialized AI agents working in harmony to protect against misinformation
          </p>
        </div>

        {/* Agents Flow */}
        <div className="relative">
          {/* Connection Lines */}
          <div className="hidden lg:block absolute top-1/2 left-0 right-0 h-0.5 bg-gradient-to-r from-primary via-secondary to-success opacity-20" />
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 relative">
            {agents.map((agent, index) => {
              const Icon = agent.icon;
              return (
                <div key={agent.id} className="relative">
                  <Card className="p-6 bg-gradient-card backdrop-blur-sm border-primary/10 hover:border-primary/30 transition-all duration-300 hover:shadow-glow hover:-translate-y-2 h-full">
                    <div className="space-y-4">
                      {/* Agent Number */}
                      <div className="flex items-center justify-between">
                        <Badge variant="outline" className="text-xs">
                          Agent {agent.id}
                        </Badge>
                        <Badge 
                          variant="outline" 
                          className="bg-success/10 text-success border-success/20 animate-pulse-glow"
                        >
                          {agent.status}
                        </Badge>
                      </div>

                      {/* Icon */}
                      <div className={`w-16 h-16 rounded-xl bg-gradient-primary flex items-center justify-center ${agent.color}`}>
                        <Icon className="w-8 h-8 text-white" />
                      </div>

                      {/* Agent Info */}
                      <div>
                        <h3 className="text-xl font-semibold text-foreground mb-2">
                          {agent.name}
                        </h3>
                        <p className="text-sm text-muted-foreground">
                          {agent.description}
                        </p>
                      </div>

                      {/* Activity Indicator */}
                      <div className="pt-4 border-t border-border">
                        <div className="flex items-center gap-2 text-xs text-muted-foreground">
                          <div className="w-2 h-2 rounded-full bg-success animate-pulse-glow" />
                          <span>Processing in real-time</span>
                        </div>
                      </div>
                    </div>
                  </Card>

                  {/* Arrow between agents */}
                  {index < agents.length - 1 && (
                    <div className="hidden lg:flex absolute top-1/2 -right-4 transform -translate-y-1/2 z-10">
                      <ArrowRight className="w-8 h-8 text-primary animate-pulse" />
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>

        {/* Workflow Description */}
        <div className="mt-16 max-w-3xl mx-auto">
          <Card className="p-8 bg-gradient-card backdrop-blur-sm border-primary/10">
            <h3 className="text-2xl font-semibold text-foreground mb-4">
              Autonomous Workflow
            </h3>
            <div className="space-y-3 text-muted-foreground">
              <p>
                <span className="font-semibold text-primary">1. Detection:</span> Continuously monitors multiple platforms for potential misinformation using advanced NLP and multimodal analysis.
              </p>
              <p>
                <span className="font-semibold text-secondary">2. Verification:</span> Cross-references flagged content with trusted databases and fact-checking sources using RAG technology.
              </p>
              <p>
                <span className="font-semibold text-accent">3. Scoring:</span> Calculates impact scores based on virality, reach, and severity to prioritize high-risk content.
              </p>
              <p>
                <span className="font-semibold text-success">4. Alerting:</span> Generates and distributes verified information to users through multiple channels instantly.
              </p>
            </div>
          </Card>
        </div>
      </div>
    </section>
  );
};

export default AgentVisualization;
