// Copyright (C) 2021 Bosutech XXI S.L.
//
// nucliadb is offered under the AGPL v3.0 and as commercial software.
// For commercial licensing, contact us at info@nuclia.com.
//
// AGPL:
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Affero General Public License as
// published by the Free Software Foundation, either version 3 of the
// License, or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU Affero General Public License for more details.
//
// You should have received a copy of the GNU Affero General Public License
// along with this program. If not, see <http://www.gnu.org/licenses/>.
//

mod metrics_service;

use std::net::SocketAddr;

use axum::routing::get;
use axum::Router;

use crate::env::metrics_http_port;

pub struct MetricsServerOptions {
    pub default_http_port: u16,
}

pub async fn run_http_metrics_server(options: MetricsServerOptions) {
    // Add routes to services
    let addr = SocketAddr::from(([0, 0, 0, 0], metrics_http_port(options.default_http_port)));
    let metrics = Router::new().route("/metrics", get(metrics_service::metrics_service));
    axum_server::bind(addr)
        // Services will be added here
        .serve(metrics.into_make_service())
        .await
        .expect("Error starting the HTTP server");
}
