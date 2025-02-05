# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.dataproc_v1.services.cluster_controller import pagers
from google.cloud.dataproc_v1.types import clusters
from google.cloud.dataproc_v1.types import operations
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from .transports.base import ClusterControllerTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import ClusterControllerGrpcAsyncIOTransport
from .client import ClusterControllerClient


class ClusterControllerAsyncClient:
    """The ClusterControllerService provides methods to manage
    clusters of Compute Engine instances.
    """

    _client: ClusterControllerClient

    DEFAULT_ENDPOINT = ClusterControllerClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ClusterControllerClient.DEFAULT_MTLS_ENDPOINT

    cluster_path = staticmethod(ClusterControllerClient.cluster_path)
    parse_cluster_path = staticmethod(ClusterControllerClient.parse_cluster_path)
    service_path = staticmethod(ClusterControllerClient.service_path)
    parse_service_path = staticmethod(ClusterControllerClient.parse_service_path)
    common_billing_account_path = staticmethod(
        ClusterControllerClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        ClusterControllerClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(ClusterControllerClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        ClusterControllerClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        ClusterControllerClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        ClusterControllerClient.parse_common_organization_path
    )
    common_project_path = staticmethod(ClusterControllerClient.common_project_path)
    parse_common_project_path = staticmethod(
        ClusterControllerClient.parse_common_project_path
    )
    common_location_path = staticmethod(ClusterControllerClient.common_location_path)
    parse_common_location_path = staticmethod(
        ClusterControllerClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ClusterControllerAsyncClient: The constructed client.
        """
        return ClusterControllerClient.from_service_account_info.__func__(ClusterControllerAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ClusterControllerAsyncClient: The constructed client.
        """
        return ClusterControllerClient.from_service_account_file.__func__(ClusterControllerAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return ClusterControllerClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> ClusterControllerTransport:
        """Returns the transport used by the client instance.

        Returns:
            ClusterControllerTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(ClusterControllerClient).get_transport_class, type(ClusterControllerClient)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, ClusterControllerTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the cluster controller client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.ClusterControllerTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = ClusterControllerClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def create_cluster(
        self,
        request: Union[clusters.CreateClusterRequest, dict] = None,
        *,
        project_id: str = None,
        region: str = None,
        cluster: clusters.Cluster = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a cluster in a project. The returned
        [Operation.metadata][google.longrunning.Operation.metadata] will
        be
        `ClusterOperationMetadata <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata>`__.

        Args:
            request (Union[google.cloud.dataproc_v1.types.CreateClusterRequest, dict]):
                The request object. A request to create a cluster.
            project_id (:class:`str`):
                Required. The ID of the Google Cloud
                Platform project that the cluster
                belongs to.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            region (:class:`str`):
                Required. The Dataproc region in
                which to handle the request.

                This corresponds to the ``region`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster (:class:`google.cloud.dataproc_v1.types.Cluster`):
                Required. The cluster to create.
                This corresponds to the ``cluster`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.dataproc_v1.types.Cluster` Describes the identifying information, config, and status of
                   a Dataproc cluster

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, region, cluster])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = clusters.CreateClusterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if region is not None:
            request.region = region
        if cluster is not None:
            request.cluster = cluster

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_cluster,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=300.0,
            ),
            default_timeout=300.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            clusters.Cluster,
            metadata_type=operations.ClusterOperationMetadata,
        )

        # Done; return the response.
        return response

    async def update_cluster(
        self,
        request: Union[clusters.UpdateClusterRequest, dict] = None,
        *,
        project_id: str = None,
        region: str = None,
        cluster_name: str = None,
        cluster: clusters.Cluster = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates a cluster in a project. The returned
        [Operation.metadata][google.longrunning.Operation.metadata] will
        be
        `ClusterOperationMetadata <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata>`__.
        The cluster must be in a
        [``RUNNING``][google.cloud.dataproc.v1.ClusterStatus.State]
        state or an error is returned.

        Args:
            request (Union[google.cloud.dataproc_v1.types.UpdateClusterRequest, dict]):
                The request object. A request to update a cluster.
            project_id (:class:`str`):
                Required. The ID of the Google Cloud
                Platform project the cluster belongs to.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            region (:class:`str`):
                Required. The Dataproc region in
                which to handle the request.

                This corresponds to the ``region`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_name (:class:`str`):
                Required. The cluster name.
                This corresponds to the ``cluster_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster (:class:`google.cloud.dataproc_v1.types.Cluster`):
                Required. The changes to the cluster.
                This corresponds to the ``cluster`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. Specifies the path, relative to ``Cluster``,
                of the field to update. For example, to change the
                number of workers in a cluster to 5, the ``update_mask``
                parameter would be specified as
                ``config.worker_config.num_instances``, and the
                ``PATCH`` request body would specify the new value, as
                follows:

                ::

                    {
                      "config":{
                        "workerConfig":{
                          "numInstances":"5"
                        }
                      }
                    }

                Similarly, to change the number of preemptible workers
                in a cluster to 5, the ``update_mask`` parameter would
                be ``config.secondary_worker_config.num_instances``, and
                the ``PATCH`` request body would be set as follows:

                ::

                    {
                      "config":{
                        "secondaryWorkerConfig":{
                          "numInstances":"5"
                        }
                      }
                    }

                Note: Currently, only the following fields can be
                updated:

                .. raw:: html

                     <table>
                     <tbody>
                     <tr>
                     <td><strong>Mask</strong></td>
                     <td><strong>Purpose</strong></td>
                     </tr>
                     <tr>
                     <td><strong><em>labels</em></strong></td>
                     <td>Update labels</td>
                     </tr>
                     <tr>
                     <td><strong><em>config.worker_config.num_instances</em></strong></td>
                     <td>Resize primary worker group</td>
                     </tr>
                     <tr>
                     <td><strong><em>config.secondary_worker_config.num_instances</em></strong></td>
                     <td>Resize secondary worker group</td>
                     </tr>
                     <tr>
                     <td>config.autoscaling_config.policy_uri</td><td>Use, stop using, or
                     change autoscaling policies</td>
                     </tr>
                     </tbody>
                     </table>

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.dataproc_v1.types.Cluster` Describes the identifying information, config, and status of
                   a Dataproc cluster

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any(
            [project_id, region, cluster_name, cluster, update_mask]
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = clusters.UpdateClusterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if region is not None:
            request.region = region
        if cluster_name is not None:
            request.cluster_name = cluster_name
        if cluster is not None:
            request.cluster = cluster
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_cluster,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=300.0,
            ),
            default_timeout=300.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            clusters.Cluster,
            metadata_type=operations.ClusterOperationMetadata,
        )

        # Done; return the response.
        return response

    async def stop_cluster(
        self,
        request: Union[clusters.StopClusterRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Stops a cluster in a project.

        Args:
            request (Union[google.cloud.dataproc_v1.types.StopClusterRequest, dict]):
                The request object. A request to stop a cluster.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.dataproc_v1.types.Cluster` Describes the identifying information, config, and status of
                   a Dataproc cluster

        """
        # Create or coerce a protobuf request object.
        request = clusters.StopClusterRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.stop_cluster,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            clusters.Cluster,
            metadata_type=operations.ClusterOperationMetadata,
        )

        # Done; return the response.
        return response

    async def start_cluster(
        self,
        request: Union[clusters.StartClusterRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Starts a cluster in a project.

        Args:
            request (Union[google.cloud.dataproc_v1.types.StartClusterRequest, dict]):
                The request object. A request to start a cluster.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.dataproc_v1.types.Cluster` Describes the identifying information, config, and status of
                   a Dataproc cluster

        """
        # Create or coerce a protobuf request object.
        request = clusters.StartClusterRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.start_cluster,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            clusters.Cluster,
            metadata_type=operations.ClusterOperationMetadata,
        )

        # Done; return the response.
        return response

    async def delete_cluster(
        self,
        request: Union[clusters.DeleteClusterRequest, dict] = None,
        *,
        project_id: str = None,
        region: str = None,
        cluster_name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a cluster in a project. The returned
        [Operation.metadata][google.longrunning.Operation.metadata] will
        be
        `ClusterOperationMetadata <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata>`__.

        Args:
            request (Union[google.cloud.dataproc_v1.types.DeleteClusterRequest, dict]):
                The request object. A request to delete a cluster.
            project_id (:class:`str`):
                Required. The ID of the Google Cloud
                Platform project that the cluster
                belongs to.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            region (:class:`str`):
                Required. The Dataproc region in
                which to handle the request.

                This corresponds to the ``region`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_name (:class:`str`):
                Required. The cluster name.
                This corresponds to the ``cluster_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

                   The JSON representation for Empty is empty JSON
                   object {}.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, region, cluster_name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = clusters.DeleteClusterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if region is not None:
            request.region = region
        if cluster_name is not None:
            request.cluster_name = cluster_name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_cluster,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=300.0,
            ),
            default_timeout=300.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=operations.ClusterOperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_cluster(
        self,
        request: Union[clusters.GetClusterRequest, dict] = None,
        *,
        project_id: str = None,
        region: str = None,
        cluster_name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> clusters.Cluster:
        r"""Gets the resource representation for a cluster in a
        project.

        Args:
            request (Union[google.cloud.dataproc_v1.types.GetClusterRequest, dict]):
                The request object. Request to get the resource
                representation for a cluster in a project.
            project_id (:class:`str`):
                Required. The ID of the Google Cloud
                Platform project that the cluster
                belongs to.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            region (:class:`str`):
                Required. The Dataproc region in
                which to handle the request.

                This corresponds to the ``region`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_name (:class:`str`):
                Required. The cluster name.
                This corresponds to the ``cluster_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dataproc_v1.types.Cluster:
                Describes the identifying
                information, config, and status of a
                Dataproc cluster

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, region, cluster_name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = clusters.GetClusterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if region is not None:
            request.region = region
        if cluster_name is not None:
            request.cluster_name = cluster_name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_cluster,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.InternalServerError,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=300.0,
            ),
            default_timeout=300.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def list_clusters(
        self,
        request: Union[clusters.ListClustersRequest, dict] = None,
        *,
        project_id: str = None,
        region: str = None,
        filter: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListClustersAsyncPager:
        r"""Lists all regions/{region}/clusters in a project
        alphabetically.

        Args:
            request (Union[google.cloud.dataproc_v1.types.ListClustersRequest, dict]):
                The request object. A request to list the clusters in a
                project.
            project_id (:class:`str`):
                Required. The ID of the Google Cloud
                Platform project that the cluster
                belongs to.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            region (:class:`str`):
                Required. The Dataproc region in
                which to handle the request.

                This corresponds to the ``region`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (:class:`str`):
                Optional. A filter constraining the clusters to list.
                Filters are case-sensitive and have the following
                syntax:

                field = value [AND [field = value]] ...

                where **field** is one of ``status.state``,
                ``clusterName``, or ``labels.[KEY]``, and ``[KEY]`` is a
                label key. **value** can be ``*`` to match all values.
                ``status.state`` can be one of the following:
                ``ACTIVE``, ``INACTIVE``, ``CREATING``, ``RUNNING``,
                ``ERROR``, ``DELETING``, or ``UPDATING``. ``ACTIVE``
                contains the ``CREATING``, ``UPDATING``, and ``RUNNING``
                states. ``INACTIVE`` contains the ``DELETING`` and
                ``ERROR`` states. ``clusterName`` is the name of the
                cluster provided at creation time. Only the logical
                ``AND`` operator is supported; space-separated items are
                treated as having an implicit ``AND`` operator.

                Example filter:

                status.state = ACTIVE AND clusterName = mycluster AND
                labels.env = staging AND labels.starred = \*

                This corresponds to the ``filter`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dataproc_v1.services.cluster_controller.pagers.ListClustersAsyncPager:
                The list of all clusters in a
                project.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, region, filter])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = clusters.ListClustersRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if region is not None:
            request.region = region
        if filter is not None:
            request.filter = filter

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_clusters,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.InternalServerError,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=300.0,
            ),
            default_timeout=300.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListClustersAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def diagnose_cluster(
        self,
        request: Union[clusters.DiagnoseClusterRequest, dict] = None,
        *,
        project_id: str = None,
        region: str = None,
        cluster_name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Gets cluster diagnostic information. The returned
        [Operation.metadata][google.longrunning.Operation.metadata] will
        be
        `ClusterOperationMetadata <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata>`__.
        After the operation completes,
        [Operation.response][google.longrunning.Operation.response]
        contains
        `DiagnoseClusterResults <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#diagnoseclusterresults>`__.

        Args:
            request (Union[google.cloud.dataproc_v1.types.DiagnoseClusterRequest, dict]):
                The request object. A request to collect cluster
                diagnostic information.
            project_id (:class:`str`):
                Required. The ID of the Google Cloud
                Platform project that the cluster
                belongs to.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            region (:class:`str`):
                Required. The Dataproc region in
                which to handle the request.

                This corresponds to the ``region`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_name (:class:`str`):
                Required. The cluster name.
                This corresponds to the ``cluster_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.dataproc_v1.types.DiagnoseClusterResults`
                The location of diagnostic output.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, region, cluster_name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = clusters.DiagnoseClusterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if region is not None:
            request.region = region
        if cluster_name is not None:
            request.cluster_name = cluster_name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.diagnose_cluster,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=300.0,
            ),
            default_timeout=300.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            clusters.DiagnoseClusterResults,
            metadata_type=operations.ClusterOperationMetadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-cloud-dataproc",).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("ClusterControllerAsyncClient",)
